terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.73.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
ami           =  data.aws_ami.packer_image.id
instance_type = "t2.micro"

tags = {
Name = "HelloWorld"
}
}




data "aws_ami" "packer_image" {
  most_recent = true

  

  owners = ["175633476877"] # Canonical
}