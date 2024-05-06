provider "aws" {
  region = "us-east-1"

}

variable "cluster_name" {
  default = "ntconsult"
}

variable "cluster_version" {
  default = "1.29"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.40"
    }
  }
}
