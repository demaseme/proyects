from abc import ABC
import boto3
from mypy_boto3_events.client import EventBridgeClient

class AbstractEventBridgeClient(ABC):
    def __init__(self, source:str, detailtype:str, eventbus:str):
        self.source = source
        self.detailtype = detailtype
        self.eventbus = eventbus
        self.eventClient:EventBridgeClient = boto3.client('events')
        
