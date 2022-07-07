CREATE OR REPLACE TABLE trips_data_all.yellow_tripdata_partitioned_table 
                                PARTITION BY DATE(tpep_pickup_datetime) AS 
                                SELECT * EXCEPT(airport_fee) FROM trips_data_all.external_yellow_tripdata_table;


CREATE OR REPLACE TABLE trips_data_all.green_tripdata_partitioned_table 
                                PARTITION BY DATE(lpep_pickup_datetime) AS 
                                SELECT * EXCEPT(ehail_fee) FROM trips_data_all.external_green_tripdata_table;