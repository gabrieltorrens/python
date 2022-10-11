import boto3
import botocore
import pprint

print("Guard check")

gdSession = boto3.session.Session(region_name="us-east-1").client(service_name="guardduty")
activeGuards = gdSession.list_detectors()

if len(activeGuards['DetectorIds']) == 0:
    print("region is unguarded")
else:
    print(f"{activeGuards['DetectorIds'][0]}, is active")