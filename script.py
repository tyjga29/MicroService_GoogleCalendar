import schedule
import time

from google_calendar_package.calendar_controller import getViableEvents
from mqtt_package.mqtt_publisher import send_events


def start_google_events():
    events = getViableEvents()
    send_events(events)

if __name__ == '__main__':
    schedule.every().day.at("01:00").do(start_google_events)

    while True:
        schedule.run_pending()
        time.sleep(1)