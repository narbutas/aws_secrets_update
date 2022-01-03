`usage: aws_secrets.py [-h] [-r REGION] [-a ACTION] [-f SECRETS_LIST_FILE] [-s SECRET_NAME]`


**_optional arguments_:**

    -h, --help                                                      show this help message and exit
    -r REGION, --region REGION                                      AWS region you want to work on: us-east-1, eu-west-1
    -a ACTION, --action ACTION
                    possible actions:
                        GET                                         Get Secret Values to file; 
                        UPDATE                                      Update existing secret with values from file putted in secrets_upload/ directory with extention _<SECRET_NAME>.secret_; 
                        GET-ALL-SECRETS-VALUES                      Get all existing secrets values from file provided with --secrets-list-file to separated files in downloaded_secrets/; 
                        UPDATE-ALL-SECRETS                          Update all secrets from file provided with --secrets-list-file with data in secrets_upload/ directory as separated files;
    -f SECRETS_LIST_FILE, --secrets-list-file SECRETS_LIST_FILE     Provide file with secret names you need to download or update
    -s SECRET_NAME, --secret-name SECRET_NAME                       Provide a file with secret names, every secret in new line

                        
