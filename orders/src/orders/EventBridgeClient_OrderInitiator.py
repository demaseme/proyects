from .EventBridgeClient import AbstractEventBridgeClient
from aws_lambda_powertools import Logger

class EventBridgeClient_OrderInitiator(AbstractEventBridgeClient):
    def __init__(self):
        super().__init__('order.publisher', 'order-data', 'OrdersEventBus')
        self.logger = Logger(service=__name__)
        self.logger.info(f'{__name__} initiaded succesfully')
        
    """
    Puts the order event in the event bridge bus so that step function orchestrator can pick it up 
    and initiate the flow.
    Returns: 0 if event was put ok, 1 ow.
    """
    def putOrderEvent(self, orderData:dict) -> None:
        response = None
        try:
            response = self.eventClient.put_events(
                Entries=[{ 
                    'Source': self.source,
                    'DetailType':self.detailtype,
                    'Detail': orderData,
                    'EventBusName': self.eventbus
                }]
            )
        except Exception as ex:
            self.logger.exception('An exception occurred')
            raise RuntimeError('Error') from ex

        return response
   
    
        