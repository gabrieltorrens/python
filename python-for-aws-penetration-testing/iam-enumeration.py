import botocore
import boto3
import pprint

print("IAM enumerator")
print("==============")

iamSession = boto3.session.Session(profile_name="scenario1",region_name='us-east-1').client(service_name='iam')

print("User list:")
users = iamSession.list_users()
for x in users['Users']:
    print(" " + x['UserName'])

print("Groups:")
groups = iamSession.list_groups()
for x in groups["Groups"]:
    print(" "+ x['GroupName'])

print("Access keys:")
keys = iamSession.list_access_keys()
for x in keys['AccessKeyMetadata']:
    print(" "+ x["UserName"]+" "+x["AccessKeyId"])