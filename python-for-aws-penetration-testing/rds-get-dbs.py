import boto3
import botocore
import pprint

ssm=boto3.session.Session().client("ssm")
regions=ssm.get_parameters_by_path(Path="/aws/service/global-infrastructure/regions") #gets a list of regions
results=regions['Parameters']

while 'NextToken' in regions: #NextToken is only returned in case you have more regions than can be returned
    regions=ssm.get_parameters_by_path(Path="/aws/service/global-infrastructure/regions", NextToken = regions['NextToken'])
    results.extend(regions['Parameters'])

for x1 in results:
    try:
        rds=boto3.session.Session(region_name=x1['Value']).client('rds')
        rdi=rds.describe_db_instances()
        for x2 in rdi['DBInstances']:
            print(" "+x2['DBInstanceIdentifier']+" "+x1['Value']+" "+x2['Engine']+" "+x2['EngineVersion'])
            print(" "+x2['Endpoint']['Address']+":"+str(x2['Endpoint']['Port']))
    except:
        pass