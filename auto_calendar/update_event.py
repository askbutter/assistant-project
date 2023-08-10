from datetime import datetime, timedelta
from calendar_setup import get_calendar_service

myevent_title = 'Automating calendar'
#year month day hour min sec
myevent_datetime = datetime(2023, 8, 11, 0, 30)

def main():
    # update the event to tomorrow 9 AM IST
    service = get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    
    d = datetime.now().date()
    tomorrow = datetime(d.year, d.month, d.day, 9)+timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=2)).isoformat()
    
    try:
        events_result = service.events().list(
            calendarId='primary', timeMin=now,
            singleEvents=True,
            orderBy='startTime').execute()
        
        events = events_result.get('items', [])
        
        if not events:
            print("No event found")
        else:
            for event in events:
                
                event_title = event.get('summary')
                start_datetime = event['start'].get('dateTime', event['start'].get('date'))
                split_start_datetime = start_datetime.rsplit('-', 1)[0]
                
                if event_title == myevent_title or split_start_datetime == myevent_datetime.isoformat():
                    print("Event match found.")
                    event_id = event['id']
                    
                    try:
                        event_result = service.events().update(
                            calendarId='primary',
                            eventId=event_id,
                            body={
                                "summary": 'Updated Automating calendar',
                                "description": 'This is a tutorial example of automating google calendar with python, updated time.',
                                "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
                                "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
                            },
                        ).execute()
                        
                        
                        print("updated event")
                        print("id: ", event_result['id'])
                        print("summary: ", event_result['summary'])
                        print("starts at: ", event_result['start']['dateTime'])
                        print("ends at: ", event_result['end']['dateTime'])
                    except googleapiclient.errors.HttpError:
                        print("Failed to delete event.")
                        
    except Exception as e:
        print("error", e)
        
if __name__ == '__main__':
    main()
