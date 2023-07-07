from .DynamoDBClient import DynamoDbClient
from aws_lambda_powertools import Logger
from datetime import date
import os

class DynamoDBClient_Orders(DynamoDbClient):
    def __init__(self):
        self.logger = Logger(service=__name__)
        super().__init__(os.environ['ORDERS_DYN_TABLE'])
        self.logger.info(f'{__name__} initiaded succesfully')

    def putNewOrder(self, order_id:str):
        try:
            self.table.put_item(
            Item={
                'OrderId':order_id,
                'CustomerId': 'NO-CUST',
                'CreationDate': date.today().strftime('%Y-%m-%d')
            }
            )
        except Exception as ex:
            self.logger.exception('Error putting new Order')
            raise RuntimeError('Error') from ex
