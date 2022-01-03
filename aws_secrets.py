import os, sys, boto3, base64, argparse, re
from botocore.exceptions import ClientError

parser = argparse.ArgumentParser()
parser.add_argument("-r", '--region', required=False, help="AWS region you want to work on: us-east-1, eu-west-1")
parser.add_argument("-a", '--action', required=True, help="""possible actions: \n
                                                                *** GET - Get Secret Values to file; \n
                                                                *** UPDATE - Update existing secret with values from file putted in secrets_upload/ directory with extention <SECRET_NAME>.secret;
                                                                *** GET-ALL-SECRETS-VALUES - Get all existing secrets values from file provided with --secrets-list-file to separated files in downloaded_secrets/; 
                                                                *** UPDATE-ALL-SECRETS - Update all secrets from file provided with --secrets-list-file with data in secrets_upload/ directory as separated files;
                                                            """)
parser.add_argument("-f", '--secrets-list-file', required=False, help="Provide file with secret names you need to download or update")
parser.add_argument("-s", '--secret-name', required=False, help="Provide a file with secret names, every secret in new line")

args = vars(parser.parse_args())

if args['region']:
    region=args['region'].lower()
else:
    region="us-east-1"
if args['secrets_list_file']:
    secrets_list_file=args['secrets_list_file']
if args['secret_name']:
    secret_name=args['secret_name']
s3_client = boto3.client("secretsmanager", region_name=f'{region}')
nextToken = None

def get_secret_value(secret_name):
    secret_value = "NA"
    try:
        get_secret_value_response = s3_client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            print(e) 
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            print(e) 
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print(e) 
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print(e) 
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            print(e) 
        else:
            print(e) 
    else:
        if 'SecretString' in get_secret_value_response:
            secret_value = get_secret_value_response['SecretString']
        else:
            secret_value = base64.b64decode(get_secret_value_response['SecretBinary'])
    return secret_value

def write_secret_to_file(secret_name):
    secret_value = get_secret_value(secret_name)
    with open(f'downloaded_secrets/{secret_name}.secret', "w") as file:
        file.writelines(secret_value)
    return f"INFO: Secret {secret_name} successful downloaded"

def update_secret_values(secret_name):
    try:
        secret_value = open(f"secrets_upload/{secret_name}.secret", "r") 
    except FileNotFoundError as e:
        return f'ERROR: {secret_name} file does not exists in secrets_upload/ directory'
    else:
        try:
            response = s3_client.put_secret_value(SecretId=f'{secret_name}', SecretString=f'{secret_value.read()}')
            return f"INFO: Secret {secret_name} successful updated"
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceNotFoundException':
                return e     

def main():
    if args['action'].lower() == 'get':
        print(f"### Downloading secret {secret_name} to downloaded_secrets/{secret_name}.secret ###")
        print(write_secret_to_file(secret_name))
    elif args['action'].lower() == 'update':
        print(f"### Updating secret {secret_name} with data from  secrets_upload/{secret_name}.secret ###")
        print(update_secret_values(secret_name))
    elif args['action'].lower() == 'get-all-secrets-values':
        print(f"### Downloading secrets from {secrets_list_file} file to secrets_upload/ ###")
        secrets_file = open(secrets_list_file, 'r')
        secrets_list = secrets_file.read().splitlines()
        for secret in secrets_list:
            print(write_secret_to_file(secret))
    elif args['action'].lower() == 'update-all-secrets':
        print(f"### Updating secrets from {secrets_list_file} with data from secrets_upload/ ###")
        secrets_file = open(secrets_list_file, 'r')
        secrets_list = secrets_file.read().splitlines()
        for secret in secrets_list:
            print(update_secret_values(secret))
    else:
        print('ERROR: Unknown action')
        sys.exit()

main()
