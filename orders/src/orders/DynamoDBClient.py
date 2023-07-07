import boto3
from abc import ABC 


class DynamoDbClient(ABC):
    def __init__(self, table_name:str) :
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)
        