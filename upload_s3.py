import boto3
from boto3 import Session
import botocore

def get_session(role_arn, name='WildfireAssumedRole', duration=900):
    """ get AWS sessions by assuming a role """

    session = Session()

    if role_arn is not None:
        sts = session.client('sts')
        role = sts.assume_role(
            RoleArn=role_arn,
            RoleSessionName=name,
            DurationSeconds=duration
        )
        aws_access_key_id = role['Credentials']['AccessKeyId']
        aws_secret_access_key = role['Credentials']['SecretAccessKey']
        aws_session_token = role['Credentials']['SessionToken']
        session = Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token
        )
    return session

s = get_session("arn:aws:iam::840551294022:role/rol-s3-dat-warehouse-ledger-tst")
config = botocore.config.Config(signature_version="s3v4")

s3_c = s.client("s3")

s3_c.put_object(Body=b'something', Bucket="s3-rpt-uss-dat-warehouse", Key="tst/ledger/05/31/2017/test1.txt")