class BaseLogHandler:
    def __init__(self, log_level, *args, **kwargs):
        self.log_level = log_level
        super().__init__(*args, **kwargs)
