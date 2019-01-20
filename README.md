# Development

## Run locally

~~~bash
python run.py
~~~

# Deployment

## Build & push

~~~bash
docker build -t dakl/particle-relay-hub-handler .
docker push dakl/particle-relay-hub-handler
~~~

## Run Container

~~~bash
docker run \
-e RELAY_HUB_DEVICE_ID=(echo $RELAY_HUB_DEVICE_ID) \
-e LEGO_HOUSE_DEVICE_ID=(echo $LEGO_HOUSE_DEVICE_ID) \
-e PARTICLE_ACCESS_TOKEN=(echo $PARTICLE_ACCESS_TOKEN) \
dakl/particle-relay-hub-handler
~~~

## Run in swarm

~~~bash
docker service create \
--replicas 1 \
--name particle-relay-hub-api \
-e RELAY_HUB_DEVICE_ID=(echo $RELAY_HUB_DEVICE_ID) \
-e LEGO_HOUSE_DEVICE_ID=(echo $LEGO_HOUSE_DEVICE_ID) \
-e PARTICLE_ACCESS_TOKEN=(echo $PARTICLE_ACCESS_TOKEN) \
dakl/particle-relay-hub-handler
~~~

# CI

Builds and pushes the image. Webhook for continuous deployment is TBD.