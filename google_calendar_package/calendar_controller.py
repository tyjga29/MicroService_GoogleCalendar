from datetime import datetime, timezone
import dateutil.parser

from google_calendar_package.google_api_requests import getEvents

ALLOWED_SUMMARIES = ["Gym", 
                     "Work", 
                     "Yoga", 
                     "Studying"]


def getViableEvents():
    events = getEvents()
    today = datetime.now(timezone.utc)

    filtered_events = []

    for event in events:
        cut_event = {}
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_datetime = dateutil.parser.parse(start)
        if event ['summary'] in ALLOWED_SUMMARIES or start_datetime <= today:
            cut_event['summary'] = event['summary']
            cut_event['start'] = start_datetime
            filtered_events.append(cut_event)

    return filtered_events


