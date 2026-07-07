from datetime import datetime, timedelta
from airflow import DAG
default_args = {'owner': 'teacher', 'start_date': datetime(2026, 7, 1)}
with DAG('student_etl_pipeline', default_args=default_args, schedule_interval='@daily', catchup=False) as dag: pass
