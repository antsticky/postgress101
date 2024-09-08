
from enum import Enum
from typing import Self, List


class RunCondition(Enum):
    ALL_SUCCESS = "ALL_SUCCESS"
    ALWAYS = "ALWAYS"

class RunState(Enum):
    SUCCESS = "Success"
    FAILED = "Failed"
    SKIPPED = "Skipped"
    PENDING = "Pending"
    RUNNING = "Running"
    
    @classmethod
    def finished(cls) -> List[Self]:
        return [cls.SUCCESS, cls.FAILED, cls.SKIPPED]