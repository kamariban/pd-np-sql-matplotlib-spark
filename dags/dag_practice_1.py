from datetime import datetime 
import os
import json
import random

from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import dag, task, get_current_context, DAG


def say_hello():
     print("Hello from Apache Airflow!")


with DAG(
    "my_first_dag",
    start_date = datetime(2026,1,1),
    schedule = None,
    catchup= False ,
    ) as dag:

    t1 = PythonOperator(
        task_id = "greet_user" ,
        python_callable = say_hello,
    )


output_path = "/Users/kamari/Documents/project_info/dags"