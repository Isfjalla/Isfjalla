provider "azure" {
  profile 	= "default"
  region 	= "us-east"
}

resource "azure_bucket" "tf_firstcourse" {
  bucket 	= "Azure-terraform-2022-03-24"
  acl	 	= "private"
}
