import paho.mqtt.client as mqtt

import json
from datetime import datetime
from json import JSONEncoder

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
    payload = {
        'events': events
    }
    payload_str = json.dumps(payload, cls=DateTimeEncoder)
    client.publish(topic, payload_str)
    client.disconnect
