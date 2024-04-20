import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from urllib import request
dag = DAG(dag_id="templateting",
          start_date=airflow.utils.dates.days_ago(3),
          schedule_interval="@hourly"
          )

def _print_context(**kwargs):
    print(kwargs)


get_data = BashOperator(
    task_id="get_data",
    #get https://dumps.wikimedia.org/other/pageviews/2019/2019-07/pageviews-20190707-110000.gz
    bash_command=("curl -o /tmp/wikipageviews.gz "
                  "https://dumps.wikimedia.org/other/pageviews/"
                  "{{ execution_date.year }}/"
                  "{{ execution_date.year }}-"
                  "{{ '{:02}'.format(execution_date.month) }}/"
                  "pageviews-{{ execution_date.year }}"
                  "{{ '{:02}'.format(execution_date.month) }}"
                  "{{ '{:02}'.format(execution_date.day) }}-"
                  "{{ '{:02}'.format(execution_date.hour) }}0000.gz"
                  ),
    dag=dag)

# templating python operator
def _get_data(execution_date):
     year, month, day, hour, *_ = execution_date.timetuple()
     url = (
     "https://dumps.wikimedia.org/other/pageviews/"
     f"{year}/{year}-{month:0>2}/"
     "pageviews-{year}{month:0>2}{day:0>2}-{hour:0>2}0000.gz"
     )
     output_path = "/tmp/wikipageviews.gz"
     request.urlretrieve(url, output_path)

get_data_python =  PythonOperator(
    task_id="python_template",
    python_callable=_get_data,
    dag = dag # no need to provide explicit context, in airflow 2 all  by default abviable all context variables

)

get_data_python2=  PythonOperator(
    task_id="python_template",
    python_callable=_get_data,
    trigger_rule="none_failed",
    dag = dag
)




