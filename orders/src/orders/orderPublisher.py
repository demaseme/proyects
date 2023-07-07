import uuid
from .EventBridgeClient_OrderInitiator import EventBridgeClient_OrderInitiator
from .DynamoDbClient_Orders import DynamoDBClient_Orders
from aws_lambda_powertools import Logger
from aws_lambda_powertools.logging import correlation_paths

ebclient_order = EventBridgeClient_OrderInitiator()
dynclient_order = DynamoDBClient_Orders()
logger = Logger(service=__name__)

@logger.inject_lambda_context(correlation_id_path=correlation_paths.LAMBDA_FUNCTION_URL, log_event=True)
def handler(event, context):
    orderId = str(uuid.uuid4())
    detailJsonString = f'{{"OrderId": "{orderId}"}}'
    print(detailJsonString)
    putOrderItem(orderId)
    putOrderEvent(detailJsonString)
    return 0

def putOrderEvent(orderJson):
    resp = ebclient_order.putOrderEvent(orderJson)
    logger.info(f'put_event result:{resp}')

def putOrderItem(orderId:str):
    dynclient_order.putNewOrder(orderId)
