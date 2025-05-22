def create_variable():
    from cmask_utils.logger import TasksLogger
    logger = TasksLogger("TASK LOGGING")
    logger.setLoggerLevel('DEBUG')
    logger.info("Iniciando criação da variável")
    value = "Olá do task1!"
    logger.info(f"Variável criada: {value}")
    return value