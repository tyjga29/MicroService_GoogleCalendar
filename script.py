from google_calendar_package.calendar_controller import getViableEvents
from mqtt_package.mqtt_publisher import send_events

events = getViableEvents()
send_events(events)