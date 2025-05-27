import boto3

# The access credentials for S3
s3 = boto3.client(
    's3',
    aws_access_key_id='AKIAYSE4OBYOF3DSL26M',
    aws_secret_access_key='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',
    region_name='ap-southeast-2'  # region
)