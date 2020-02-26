import datetime as dt 
from airflow import DAG
from airflow.operators.bash_operator import BashOperator 
from airflow.python_operator import PythonOperator 

def greet():
    print('Writing in file')
    with open('greet.txt', 'a+', encoding = 'utf8') as f:
        now = dt.datetime.now() 
        t = now.strftime("%Y-%m-%d %H:%M")
        f.write(str(t) + '\n')
    return 'Greeted'

def respond():
    return 'Greet Responded Again'