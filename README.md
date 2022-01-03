`usage: aws_secrets.py [-h] -u USERNAME [-l LOCATION] [-r REGION] [-a ACTION] [-f SECRETS_LIST_FILE] [-s SECRET_NAME]`


**_optional arguments_:**

    -h, --help                                                      show this help message and exit
    -u USERNAME, --username USERNAME                                Provide your USBank username
    -l LOCATION, --location LOCATION                                Location where you from: US, EU
    -r REGION, --region REGION                                      AWS region you want to work on: us-east-1, eu-west-1
    -a ACTION, --action ACTION
                    possible actions:
                        GET                                         Get Secret Values to file; 
                        UPDATE                                      Update existing secret with values from file putted in secrets_upload/ directory with extention _<SECRET_NAME>.secret_; 
                        GET-ALL-SECRETS-VALUES                      Get all existing secrets values to file; 
                        UPDATE-ALL-SECRETS                          Update all existing secrets existing in secrets_upload/ directory as separated files;
    -f SECRETS_LIST_FILE, --secrets-list-file SECRETS_LIST_FILE     Provide file with secret names you need to download or update
    -s SECRET_NAME, --secret-name SECRET_NAME                       AWS region you want to work on: us-east-1, eu-west-1

                        
