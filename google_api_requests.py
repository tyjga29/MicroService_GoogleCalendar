import datetime

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google_api_token import getCreds

# Returns 20 Events
def getEvents():
    creds = getCreds()
    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=20, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return
        else:
            return events

    except HttpError as error:
        print('An error occurred: %s' % error)