import boto3

def lambda_handler(event, context):
    s3_client = boto3.client('s3')

    # Get the source bucket and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Copy the object to the destination bucket
    destination_bucket = 'xdest.ahmedalimsoliman.click'
    s3_client.copy_object(Bucket=destination_bucket, Key=object_key, CopySource={'Bucket': source_bucket, 'Key': object_key})

    return {
        'statusCode': 200,
        'body': 'Object copied successfully'
    }
