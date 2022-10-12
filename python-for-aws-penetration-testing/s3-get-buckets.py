import boto3
import botocore
import pprint

s3=boto3.session.Session().client('s3')
buckets = s3.list_buckets() #returns a list called 'Buckets'

#pprint.pprint(buckets)

for i in buckets['Buckets']:
    print("Bucket found: "+i['Name'])