import boto3
import botocore
import pprint

smSession = boto3.session.Session().client("secretsmanager")
print("Secrets:")

secList=smSession.list_secrets()
pprint.pprint(secList)

pwd = smSession.get_random_password(PasswordLength=16)
pprint.pprint(pwd)

adminPass = smSession.create_secret(Name="adminpw",SecretString=pwd['RandomPassword'])
pwd = smSession.get_secret_value(SecretId='adminpw')
pprint.pprint("admin password is "+pwd['SecretString'])