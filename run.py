import paho.mqtt.client as mqtt

import structlog
from app import config
from app.accessories import ACCESSORIES

logger = structlog.getLogger(__name__)

# The callback for when the client receives a CONNACK response from the server.
logger.info("Starting particle-relay-hub-api")


def on_connect(client, userdata, flags, rc):
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe('commands/relay/#')
    logger.info("Connected", rc=str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8")).strip()
    accessory_id = int(message.topic.split('/')[-1])
    logger.info('Message recieved', topic=message.topic, payload=payload)

    accessory = ACCESSORIES.get(accessory_id)
    accessory.handler(payload=payload)
    client.publish(
        topic=f'events/relay/{accessory_id}', payload=payload, retain=True)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(config.BROKER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
