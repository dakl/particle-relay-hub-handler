import paho.mqtt.client as mqtt

import structlog
from app import config
from app.accessories import ACCESSORIES
from app.handler import on_connect, on_message

logger = structlog.getLogger(__name__)

# The callback for when the client receives a CONNACK response from the server.
logger.info("Starting particle-relay-hub-api")

if not config.TOPIC_NAME:
    raise ValueError("The environment variable 'TOPIC_NAME' needs to be set.")



logger.info('Connecting to MQTT')
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(config.BROKER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
