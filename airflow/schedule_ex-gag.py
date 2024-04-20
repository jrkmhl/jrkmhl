import airflow

import datetime as dt
from airflow import DAG
dag = DAG(
    dag_id="schedule_task",
    schedule_interval="@daily",
    start_date= dt.datetime(year=2019,month=2,day=10),
    end_date=dt.datetime(year=2025,month=10,day=30)
)

# * * day mont day of wee