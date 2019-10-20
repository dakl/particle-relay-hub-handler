from flask import Flask, json
from time import sleep, time
api = Flask(__name__)


@api.route('/<device>/<id>', methods=['GET', 'POST'])
def get_base(device, id):
  start_time = time()
  sleep(2)
  elapsed = time() - start_time
  return json.dumps({'id': id, 'device': device, 'elapsed': elapsed})


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8099)
