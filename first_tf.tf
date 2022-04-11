provider "aws" {
  profile 	= "default"
  region 	= "us-east-2"
}

resource "aws_s3_bucket" "tf_firstcourse" {
  bucket 	= "aws-tf-2022-04-10"
  acl	 	= "private"
}
