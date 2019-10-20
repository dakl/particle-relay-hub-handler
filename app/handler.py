import asyncio
import time

import structlog
from gmqtt import Client as MQTTClient
from gmqtt.mqtt.constants import MQTTv311
from app import config
from app.accessories import ACCESSORIES

logger = structlog.getLogger(__name__)

STOP = asyncio.Event()


def on_connect(client, userdata, flags, rc):
    topic = f'commands/{config.TOPIC_NAME}/#'
    logger.info('Subscribing', topic=topic)
    client.subscribe(topic)
    logger.info("Connected", rc=str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8")).strip()
    logger.info('Handling message', topic=message.topic, payload=payload)

    accessory_id = int(message.topic.split('/')[-1])
    accessory = ACCESSORIES.get(f'{config.TOPIC_NAME}/{accessory_id}')
    accessory.handler(payload=payload)

    publish_topic = f'events/{config.TOPIC_NAME}/{accessory_id}'
    logger.info("Publishing state update message",
                topic=publish_topic,
                payload=payload)
    client.publish(topic=publish_topic, payload=payload, retain=True)


def on_connect_gmqtt(client, flags, rc, properties):
    topic = f'commands/{config.TOPIC_NAME}/#'
    logger.info('Subscribing', topic=topic)
    client.subscribe(topic, qos=0)
    logger.info("Connected", rc=str(rc))


def on_disconnect(client, packet, exc=None):
    logger.info('Disconnected')


def on_subscribe(client, mid, qos):
    logger.info('SUBSCRIBED')


def ask_exit(*args):
    STOP.set()


async def on_message_gmqtt(client, topic, payload, qos, properties):
    #payload = str(message.payload.decode("utf-8")).strip()
    logger.info('Handling message', topic=topic, payload=payload)

    accessory_id = int(topic.split('/')[-1])
    accessory = ACCESSORIES.get(f'{config.TOPIC_NAME}/{accessory_id}')
    await accessory.handler(payload=payload)

    publish_topic = f'events/{config.TOPIC_NAME}/{accessory_id}'
    logger.info("Publishing state update message",
                topic=publish_topic,
                payload=payload)
    client.publish(message_or_topic=publish_topic, payload=payload, retain=True)


async def start_handler(broker_host):
    logger.info("Starting handler")
    client = MQTTClient("particle-relay-hub-handler")

    client.on_connect = on_connect_gmqtt
    client.on_message = on_message_gmqtt
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe

    await client.connect(broker_host, version=MQTTv311)

    client.publish('TEST/TIME', str(time.time()), qos=1)

    await STOP.wait()
    await client.disconnect()
