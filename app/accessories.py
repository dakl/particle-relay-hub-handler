from typing import Dict

from app.accessory.base import Accessory
from app.accessory.relay import Relay
from app.accessory.lego_house_light import LegoHouseLight

ACCESSORIES: Dict[int, Accessory] = {
    1:
    Relay(
        name='relay-hub-1',
        internal_id='r1'),
    2:
    Relay(
        name='relay-hub-2',
        internal_id='r2'),
    3:
    Relay(
        name='relay-hub-3',
        internal_id='r3'),
    4:
    Relay(
        name='relay-hub-4',
        internal_id='r4'),
    5:
    LegoHouseLight(
        name='lego-house-0',
        internal_id=0),
    6:
    LegoHouseLight(
        name='lego-house-1',
        internal_id=1),
    7:
    LegoHouseLight(
        name='lego-house-2',
        internal_id=2),
    8:
    LegoHouseLight(
        name='lego-house-3',
        internal_id=3),
}
