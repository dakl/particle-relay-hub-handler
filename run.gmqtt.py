import structlog
from gmqtt import Client as MQTTClient
import asyncio, signal
from app import config
from app.handler import start_handler, ask_exit

logger = structlog.getLogger(__name__)

logger.info("Starting particle-relay-hub-api")

if not config.TOPIC_NAME:
    raise ValueError("The environment variable 'TOPIC_NAME' needs to be set.")

logger.info('Connecting to MQTT')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, ask_exit)
    loop.add_signal_handler(signal.SIGTERM, ask_exit)
    loop.run_until_complete(start_handler(config.BROKER))
