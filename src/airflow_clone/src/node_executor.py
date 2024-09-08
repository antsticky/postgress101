from datetime import datetime


class Executor:
    def __init__(self):
        self.xargs = None
        self.sys_xargs = {
            "set_xargs": self.set_xargs,
            "get_xargs": self.get_xargs}
        self.execution_start = datetime.now()

    def get_xargs(self, xargs):
        if xargs is None:
            return self.sys_xargs

        return {**{xarg: self.xargs[xarg] for xarg in xargs}, **self.sys_xargs}

    def set_xargs(self, name, value):
        if self.xargs is None:
            self.xargs = {name: value}
        else:
            self.xargs = {**self.xargs, **{name: value}}

    def execute(self, start_node):
        start_node.run(**self.get_xargs(start_node.xargs))

        operations = start_node.next_operations
        while operations is not None:
            next_operations = None

            for operation in operations:
                operation.run(**self.get_xargs(operation.xargs))

                if operation.next_operations is not None:
                    if next_operations is None:
                        next_operations = operation.next_operations
                    else:
                        next_operations.extend(operation.next_operations)

            operations = next_operations

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        print(
            f"\nTotal Execution time: {datetime.now() - self.execution_start}")
