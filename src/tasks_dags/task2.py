from tasks_dags.task_base import TaskBase

class Task2(TaskBase):
    def __init__(self, index: int):
        super().__init__(index)
    
    def print_variable(self, valor):
        self.logger.info(f"Valor recebido da task1: {valor}")
        print(f"[task2] Valor recebido da task1: {valor}")

def task2_callable(valor):
    from tasks_dags.task2 import Task2
    task = Task2(2)
    return task.print_variable(valor)
