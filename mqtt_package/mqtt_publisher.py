import paho.mqtt.client as mqtt
import json
from datetime import datetime
from json import JSONEncoder
import time
import os
import yaml

dir_path = os.path.dirname(os.path.realpath(__file__))
yaml_path = os.path.join(dir_path, 'mqtt_resources.yaml')
with open(yaml_path, 'r') as f:
    data = yaml.safe_load(f)
    mqtt_data = data["mqtt_resources"]

broker_address = mqtt_data["BROKER_ADDRESS"]
broker_port = mqtt_data["BROKER_PORT"]
topic = mqtt_data["TOPIC"]

class DateTimeEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return super(DateTimeEncoder, self).default(o)

def send_events(events):
    client = mqtt.Client()
    client.username_pw_set("pda_user","pda_password")
    client.connect(broker_address, broker_port)
    # Add a delay to allow time for the connection to establish
    time.sleep(2)  # Adjust the delay time as needed
    payload = {
        'events': events
    }
    payload_str = json.dumps(payload, cls=DateTimeEncoder)
    client.publish(topic, payload_str)
    client.disconnect
