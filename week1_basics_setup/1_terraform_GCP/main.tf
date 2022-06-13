terraform {
    required_version = ">=1.0"
    backend "local" {}
    required_providers {
        google = {
            source = "hashicorp/google"
        }
    }
}

provider "google" {
    project = var.project
    region = var.region 
    // credentials = file(var.credentials) #Use this if you do not want to set environment variable i.e GOOGLE_APPLICATION_CREDENTIALS
}

#Data Lake Bucket
# Reference : https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket

resource "google_storage_bucket" "data-lake-bucket" {
    name = "${local.data_lake_bucket}_${var.project}" # concatenating DL bucket & project name for unique name
    location = var.region

    #Optional but recommended setting
    storage_class = var.storage_class
    uniform_bucket_level_access = true

    versioning {
        enabled = true
    }

    lifecycle_rule {
        action{
            type = "Delete"
        }
        condition {
            age = 30 //days
        }
    }
    force_destroy = true
}

#Data Ware House
# Reference : https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset
resource "google_bigquery_dataset" "dataset" {
    dataset_id = var.BQ_DATASET
    project = var.project
    location = var.region
}