from typing import Dict

from app.accessory.base import Accessory
from app.accessory.relay import Relay
from app.accessory.lego_house_light import LegoHouseLight

ACCESSORIES: Dict[int, Accessory] = {
    'relay/1': Relay(name='relay-hub-1', internal_id='1'),
    'relay/2': Relay(name='relay-hub-2', internal_id='2'),
    'relay/3': Relay(name='relay-hub-3', internal_id='3'),
    'relay/4': Relay(name='relay-hub-4', internal_id='4'),
    'lego/1': LegoHouseLight(name='lego-house-1', internal_id='1'),
    'lego/2': LegoHouseLight(name='lego-house-2', internal_id='2'),
    'lego/3': LegoHouseLight(name='lego-house-3', internal_id='3'),
    'lego/4': LegoHouseLight(name='lego-house-4', internal_id='4'),
}
