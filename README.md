# Lambda with Terraform

This examples shows how to deploy the anagram function on AWS Lambda function using Terraform only.
The function is activated every time a ‘anagram.csv’ is upload to a bucket called
“anagram-fd-testing-new”.
anagram-fd-testing was already taken.

To run, configure your AWS provider as described in https://www.terraform.io/docs/providers/aws/index.html

Running the code

run `terraform init` to initialize.

run `terraform apply` to see it work.

