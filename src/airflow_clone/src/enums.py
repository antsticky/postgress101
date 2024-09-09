from enum import StrEnum
from typing import List, Self


class RunCondition(StrEnum):
    ALL_SUCCESS = "ALL_SUCCESS"
    ALWAYS = "ALWAYS"


class RunState(StrEnum):
    SUCCESS = "Success"
    FAILED = "Failed"
    SKIPPED = "Skipped"
    PENDING = "Pending"
    RUNNING = "Running"

    @classmethod
    def finished(cls) -> List[Self]:
        return [cls.SUCCESS, cls.FAILED, cls.SKIPPED]


if __name__ == "__main__":
    run_condition = RunCondition.ALL_SUCCESS

    print(run_condition)
    print(type(run_condition))
    print(f"Run Condition: {run_condition}")
