import os
import boto3

def handler(event, context):
    source_bucket = os.environ['INPUT_BUCKET']
    destination_bucket = os.environ['OUTPUT_BUCKET']

    s3_client = boto3.client('s3')

    # List all objects in the source bucket
    response = s3_client.list_objects_v2(Bucket=source_bucket)

    # Iterate over each object in the source bucket
    for obj in response['Contents']:
        object_key = obj['Key']

        # Copy the object to the destination bucket
        s3_client.copy_object(Bucket=destination_bucket, Key=object_key, CopySource={'Bucket': source_bucket, 'Key': object_key})

    return {
        'statusCode': 200,
        'body': 'All existing objects have been copied to the destination bucket.'
    }
