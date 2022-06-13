FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow fastparquet

WORKDIR /app
COPY Data_ingestion.py Data_ingestion.py

ENTRYPOINT [ "python", "Data_ingestion.py" ]