def print_variable(ti):
    from cmask_utils.logger import TasksLogger
    logger = TasksLogger("TASK LOGGING")
    logger.setLoggerLevel('DEBUG')
    valor = ti.xcom_pull(task_ids='task1')
    logger.info(f"Valor recebido da task1: {valor}")
    print(f"Valor recebido da task1: {valor}")