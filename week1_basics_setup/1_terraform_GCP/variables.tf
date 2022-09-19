locals {
    data_lake_bucket = "dtc_data_lake"
}

variable "project" {
    description = "eminent-clock-362719"
}

variable "region" {
    description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
    default = "us-east1"
    type = string
}

variable "storage_class" {
    description = "Storage class type for your bucket"
    default = "STANDARD"
}

variable "BQ_DATASET" {
    description = "BQ dataset that raw data (from GCS) will be written to"
    type = string
    default = "trips_data_all"
}