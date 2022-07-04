### first we will import libraries required for the DAG.
#import os
#import logging
#
#from airflow import DAG
#from airflow.utils.dates import days_ago
#from airflow.utils.task_group import TaskGroup 
#
#from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator, BigQueryInsertJobOperator
#from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator
#
#PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
#BUCKET = os.environ.get("GCP_GCS_BUCKET")
#
#path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
#BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", 'trips_data_all')
#
#DATASET = "tripdata"
#YEAR_RANGE = {2019, 2020, 2021, 2022}
#COLOUR_RANGE = {'yellow': 'tpep_pickup_datetime', 'green': 'lpep_pickup_datetime'}
#INPUT_PART = "raw"
#INPUT_FILETYPE = "parquet"
#
#default_args = {
#    "owner" : "airflow",
#    "start_date" : days_ago(1),
#    "depends_on_past" : False,
#    "retries" : 1,
#}
#
### DAG declaration - using a context manager (an implicit way)
#with DAG(
#    dag_id = "live_coded_dag",
#    schedule_interval = "@daily",
#    default_args = default_args,
#    catchup = False,
#    max_active_runs = 1,
#    tags = ['dtc-de'],
#) as dag:
#    
#    for year in YEAR_RANGE:
#
#        gcs_2_gcs_task = GCSToGCSOperator(
#            task_id = 'task1',
#            source_bucket=BUCKET,
#            source_object="raw/yellow_trip_data/{year}/yellow_tripdata_*.parquet",
#            destination_bucket="yellow/",
#            move_object=True,
#        )
#
#        #gcs_2_bq_ext = BigQueryCreateExternalTableOperator(
#        #    task_id="bigquery_external_table_task",
#        #    table_resource={
#        #        "tableReference": {
#        #            "projectId": PROJECT_ID,
#        #            "datasetId": BIGQUERY_DATASET,
#        #            "tableId": "external_yellow_tripdata",
#        #        },
#        #        "externalDataConfiguration": {
#        #            "sourceFormat": "PARQUET",
#        #            "sourceUris": [f"gs://{BUCKET}/yellow/*"],
#        #        },
#        #    },
#        #)
##
#        #CREATE_PART_TBL_QUERY = f"CREATE OR REPLACE TABLE {BIGQUERY_DATASET}.yellow_tripdata_partitoned \
#        #                        PARTITION BY DATE(tpep_pickup_datetime) AS \
#        #                        SELECT * FROM {BIGQUERY_DATASET}.external_yellow_tripdata;"
##
#        #bq_ext_2_part_task = BigQueryInsertJobOperator(
#        #    task_id="insert_query_job",
#        #    configuration={
#        #    "query": {
#        #            "query": CREATE_PART_TBL_QUERY,
#        #            "useLegacySql": False,
#        #        }   
#        #    },
#        #)
##
#        gcs_2_gcs_task
#        #gcs_2_bq_ext >> bq_ext_2_part_task