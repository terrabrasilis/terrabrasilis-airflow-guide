from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator, PythonOperator
from datetime import datetime

from tasks_dags.task1 import create_variable
from tasks_dags.task2 import print_variable

default_args = {
    'start_date': datetime(2025, 1, 1),
}

with DAG('exemplo_python_virtualenv_logger',
         schedule_interval=None,
         default_args=default_args,
         catchup=False) as dag:

    task1 = PythonVirtualenvOperator(
        task_id="task1",
        python_callable=create_variable,
        requirements=["/opt/airflow/projects/virtual-env-test/dist/tasks_dags-0.1.0.tar.gz"],
        system_site_packages=False,
    )

    task2 = PythonOperator(
        task_id="task2",
        python_callable=print_variable,
        provide_context=True,
    )

    task1 >> task2