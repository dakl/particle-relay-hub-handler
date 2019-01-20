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
    client.subscribe('commands/window/switch/#')
    client.subscribe('commands/lego/switch/#')
    logger.info("Connected", rc=str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8")).strip()
    logger.info("Payload parsed", payload=payload)
    accessory_id = int(message.topic.split('/')[-1])
    accessory = ACCESSORIES.get(accessory_id)
    accessory.handler(payload=payload)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(config.BROKER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
