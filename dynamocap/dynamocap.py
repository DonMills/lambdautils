###############################
## DRM 03/23/16
## Modifies Dynamodb read/write capacities
###############################
import boto3
##########################
## put tables to be modified in the following list
## format is [name, read, write]
##########################

tables = [["testscore",100,100],["gametime",100,100]]

def lambda_handler(event, context):
    results = ""
    for entry in tables:
        dbname, read, write = entry
        dbconn = boto3.resource('dynamodb').Table(dbname)
        result =  dbconn.update(
            ProvisionedThroughput={
            'ReadCapacityUnits': read,
            'WriteCapacityUnits': write
            }
        )
        msg = "Modified table {0} to read/write capacity of {1} reads and {2} writes per sec\n".format(dbname,read,write)
        print msg
        results = results + msg 
    return results
