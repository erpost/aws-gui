import boto3
import os
from shutil import move
from botocore.exceptions import ClientError


def getsession(username, mfa_code):
    creds = os.path.expanduser('~/.aws/credentials')
    creds_bak = os.path.expanduser('~/.aws/credentials.python.backup')

    # move backup credentials file if it exists
    if os.path.isfile(creds_bak):
        move(creds_bak, creds)

    if len(username) < 1:
        print('\nUsername cannot be empty! Exiting...')
        exit(1)

    # instantiate client and get device ARN
    try:
        iam_client = boto3.client('iam')
        iam_response = iam_client.list_mfa_devices(UserName=username)
        mfa_arn = iam_response['MFADevices'][0]['SerialNumber']
    except ClientError as ce:
        if ce.response['Error']['Code'] == 'NoSuchEntity':
            print('\nUsername does not exist! Exiting...')
            exit(1)
        else:
            print('\nUnknown error. Exiting...')
            exit(1)

    if len(mfa_code) != 6:
        print('\nIncorrect MFA Length. Exiting...')
        exit(1)

    # instantiate client and get session credentials and token
    try:
        sts_client = boto3.client('sts')
        sts_response = sts_client.get_session_token(SerialNumber=mfa_arn, TokenCode=mfa_code)
        print('\nSession Token successful!')

    except ClientError as ce:
        if ce.response['Error']['Code'] == 'AccessDenied':
            print('\nIncorrect MFA Code. Exiting...')
            exit(1)
        else:
            print('\nUnknown error. Exiting...')

    # backup credentials file and write new session token credentials
    move(creds, creds_bak)

    # write new credentials file
    with open(creds, 'w') as credfile:
        credfile.write('[default]\n' +
                   'aws_access_key_id = {}\n'.format(sts_response['Credentials']['AccessKeyId']) +
                   'aws_secret_access_key = {}\n'.format(sts_response['Credentials']['SecretAccessKey']) +
                   'aws_session_token = {}'.format(sts_response['Credentials']['SessionToken']))


if __name__ == "__main__":
    user_name = input('Input your AWS Username: ')
    mfa_code = input('Input your MFA Token: ')
    getsession(user_name, mfa_code)
