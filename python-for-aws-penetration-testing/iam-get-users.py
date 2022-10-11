import boto3
import botocore
import pprint

print("List users")
print("=============")

#Use two sessions to talk to two regions or use 2 differnt creds.
mySession = boto3.session.Session(profile_name="scenario1", region_name = "us-west-2")
iamSession = mySession.client(service_name="iam")
iamUsers = iamSession.list_users() #returns "Users" dictionary, https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html

for person in iamUsers["Users"]: 
    print(person['UserName']) #print UserName values