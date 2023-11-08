from calendar_controller import getViableEvents
from mqtt_broker import send_events

events = getViableEvents()
send_events(events)