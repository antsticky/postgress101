from typing import Callable, List, Self

from airflow_clone.src.enums import RunCondition, RunState


class ExecutionNode:
    def __init__(
        self,
        name: str,
        python_operator: Callable,
        run_condition: RunCondition = RunCondition.ALL_SUCCESS,
        configs: dict = None,
        xargs: list = None,
    ):
        self.name = name

        self.state: RunState = None
        self.prev_operations: List[Self] = None
        self.next_operations: List[Self] = None

        self.xargs = xargs
        self.configs = configs
        self.run_condition = run_condition
        self.python_operation = python_operator

    def __repr__(self) -> str:
        return self.name

    def select_input_xargs(self, full_xargs):
        return {
            k: v
            for k, v in full_xargs.items()
            if k in self.python_operation.__code__.co_varnames
        }

    def _run(self, **xargs):
        try:
            self.state = RunState.RUNNING
            config_dict = {} if self.configs is None else self.configs
            inputs = self.select_input_xargs({**config_dict, **xargs})
            self.python_operation(**inputs)
            self.state = RunState.SUCCESS
        except Exception as e:
            print(e)
            self.state = RunState.FAILED

    def run(self, **kwargs):
        if self.state in RunState.finished():
            return

        print(f"----------------------------\nStart {self.name}...")
        if self.run_condition == RunCondition.ALWAYS:
            self._run(**kwargs)
        elif self.run_condition == RunCondition.ALL_SUCCESS:
            if (self.prev_operations is None) or all(
                [
                    prev_operation.state == RunState.SUCCESS
                    for prev_operation in self.prev_operations
                ]
            ):
                self._run(**kwargs)
            else:
                self.state = RunState.SKIPPED
        else:
            raise NotImplementedError(
                f"Unknown run condition {self.run_condition}")
        print(
            f"End {self.name} with status {self.state}...\n----------------------------"
        )

    def __rshift__(self, other: Self):
        if self.next_operations is None:
            self.next_operations = [other]
        else:
            self.next_operations.append(other)

        if other.prev_operations is None:
            other.prev_operations = [self]
        else:
            other.prev_operations.append(self)

        return other
