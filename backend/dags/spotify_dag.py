from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from app.credentials import auth
from app.database import database

# Default arguments for the DAG
default_args = {
    "owner": "wsdpl",
    "depends_on_past": False,
    "start_date": datetime.now(),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

# Create the DAG instance
dag = DAG(
    "spotify_data_sync",
    default_args=default_args,
    description="DAG to sync Spotify data to the database",
    schedule_interval=timedelta(hours=1.03),  # Run the DAG every hour
)

# Define the tasks

# Task 1: Generate the access token
get_token_task = PythonOperator(
    task_id="generate_access_token",
    python_callable=auth.generate_access_token,
    dag=dag,
)

# Task 2: Retrieve data from Spotify and save to the database
save_data_task = PythonOperator(
    task_id="save_top_songs",
    python_callable=database.save_top_songs,
    dag=dag,
)

# Set the task dependencies
get_token_task >> save_data_task
