import boto3
import json
import sys

def delete_and_empty_versioned_bucket(bucket_name):
    # Create a Boto3 session
    session = boto3.Session(profile_name='default')

    # Create an S3 client using the session
    s3_client = session.client('s3')

    # List all object versions in the bucket
    response = s3_client.list_object_versions(Bucket=bucket_name)

    # Check if the response contains versions
    if 'Versions' in response:
        versions = response['Versions']

        # Delete each object version
        for version in versions:
            s3_client.delete_object(
                Bucket=bucket_name,
                Key=version['Key'],
                VersionId=version['VersionId']
            )

    # Check if the response contains delete markers
    if 'DeleteMarkers' in response:
        delete_markers = response['DeleteMarkers']

        # Delete each delete marker
        for delete_marker in delete_markers:
            s3_client.delete_object(
                Bucket=bucket_name,
                Key=delete_marker['Key'],
                VersionId=delete_marker['VersionId']
            )

    print(f"The bucket '{bucket_name}' has been emptied if version in enabled.")

    s3_client.delete_bucket(Bucket=bucket_name)

    print(f"The bucket '{bucket_name}' has been deleted.")



def list_bucket_generic():
    # Create a Boto3 session
    session = boto3.Session(profile_name='default')

    # Create an S3 client using the session
    s3_client = session.client('s3')

    try:
        response = s3_client.list_buckets()

        # convert to json
        bucket_names = [bucket['Name'] for bucket in response['Buckets']]
        
        for name in bucket_names:
            print(name)
    except Exception as e:
        print(e)

def list_and_delete_buckets():
    # Create a Boto3 session
    session = boto3.Session(profile_name='default')

    # Create an S3 client using the session
    s3_client = session.client('s3')

    try:
        response = s3_client.list_buckets()

        # convert to json
        bucket_names = [bucket['Name'] for bucket in response['Buckets']]
        
        for name in bucket_names:
            if "ahmedalimsoliman.click" not in name:
                delete_and_empty_versioned_bucket(name)
    except Exception as e:
        print(e)

def list_s3_buckets_with_regions():
    session = boto3.Session(profile_name='default')

    s3_client = session.client('s3')

    try:
        # Call the list_buckets method to get a list of all buckets
        response = s3_client.list_buckets()

        # Print the bucket names and their regions
        for bucket in response['Buckets']:
            bucket_name = bucket['Name']
            bucket_region = s3_client.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
            if bucket_region is None:
                pass
                # bucket_region = 'us-east-1'  # Default region if no specific location constraint is found
            print(f"Bucket: {bucket_name}, Region: {bucket_region}")

    except Exception as e:
        print(f"Error: {str(e)}")


def check_bucket_exsistance(bucket_name):
    # Create a Boto3 session
    session = boto3.Session(profile_name='default')

    # Create an S3 client using the session
    s3_client = session.client('s3')

    try:
        response = s3_client.list_buckets()

        # convert to json
        bucket_names = [bucket['Name'] for bucket in response['Buckets']]
        
        for name in bucket_names:
            if name == bucket_name:
                print("bucket exists")
                return True
        print("bucket does not exist")
        return False
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # # Check if bucket name is provided as a command line argument
    # if len(sys.argv) < 2:
    #     print("Usage: python script_name.py <bucket_name>")
    #     sys.exit(1)

    # # Get the bucket name from command line argument
    # bucket_name = sys.argv[1]



    # list_bucket_generic()
    # list_s3_buckets_with_regions()
    # check_bucket_exsistance("dd")
    list_and_delete_buckets()
    # check_bucket_esists("www.ahmedalimsoliman.eclick")