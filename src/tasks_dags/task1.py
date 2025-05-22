from tasks_dags.task_base import TaskBase

class Task1(TaskBase):
    def __init__(self, index: int):
        super().__init__(index)

    def create_variable(self):
        value = f"Olá do task1! Index: {self.index}"
        self.logger.info(f"Variável criada: {value}")
        return value

def task1_callable():
    from tasks_dags.task1 import Task1
    task = Task1(1)
    return task.create_variable()
