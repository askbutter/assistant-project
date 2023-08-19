from calendar_setup import get_calendar_service
from datetime import datetime, timedelta


def main():

    service = get_calendar_service()   
    
    event = {
        'summary': 'first class',
        'description': 'class description',
        'start': {
            'dateTime': '2023-08-18T1:00:00',
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': '2023-08-18T2:00:00',
            'timeZone': 'America/New_York',
        },
        'recurrence': [
            # MO WE FR 
            'RRULE:FREQ=WEEKLY;BYDAY=TU,TH;UNTIL=20231210T000000Z',
        ],
    }

    try:
        event_result = service.events().insert(calendarId='primary',
                                               body=event).execute()

    except Exception as e:
        print("error", e)
        
if __name__ == '__main__':
   main()
