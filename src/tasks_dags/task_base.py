from cmask_utils.logger import TasksLogger


class TaskBase:

        logger = None
        index : int = None

        def __init__(self, index: int):
                self.logger = TasksLogger("TASK LOGGING")
                self.logger.setLoggerLevel("DEBUG")
                self.index = index
