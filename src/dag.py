from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator
from datetime import datetime

from tasks_dags.task1 import task1_callable
from tasks_dags.task2 import task2_callable

default_args = {
    'start_date': datetime(2025, 1, 1),
}

requirements = [
    "/opt/airflow/projects/virtual-env-test/dist/tasks_dags-0.1.0.tar.gz"
]

with DAG('exemplo_python_virtualenv_logger',
    schedule_interval=None,
    default_args=default_args,
    catchup=False) as dag:
        
    task1 = PythonVirtualenvOperator(
        task_id="task1",
        python_callable=task1_callable,
        requirements=requirements,
        system_site_packages=False,
    )
    
    task2 = PythonVirtualenvOperator(
        task_id='task2',
        python_callable=task2_callable,
        requirements=requirements,
        system_site_packages=False,
        op_kwargs={
            'valor': task1.output
        }
    )
    
    task1 >> task2