import paho.mqtt.client as mqtt


client = mqtt.Client('test-client')
client.connect('localhost')

client.publish('commands/relay/1', 'ON', qos=1)
client.publish('commands/relay/2', 'OFF', qos=1)

