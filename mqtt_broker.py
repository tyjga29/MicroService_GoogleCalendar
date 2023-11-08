import paho.mqtt.client as mqtt
import json
from datetime import datetime
from json import JSONEncoder
import time

broker_address = "localhost"
broker_port =  1883
topic = "calendarEvents"

class DateTimeEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return super(DateTimeEncoder, self).default(o)

def send_events(events):
    client = mqtt.Client()
    client.connect(broker_address, broker_port)
    # Add a delay to allow time for the connection to establish
    time.sleep(2)  # Adjust the delay time as needed
    payload = {
        'events': events
    }
    payload_str = json.dumps(payload, cls=DateTimeEncoder)
    client.publish(topic, payload_str)
    client.disconnect
