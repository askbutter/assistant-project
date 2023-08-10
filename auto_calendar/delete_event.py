## Script to delete events from google calendar
from calendar_setup import get_calendar_service
from datetime import datetime, timedelta

myevent_title = 'Updated Automating calendar'

#year month day hour min sec
def format_24hrs(year, month, day, time_input):
    time_12hrs = datetime.strptime(time_input, "%I:%M %p")
    time_24hrs = datetime.strftime(time_12hrs, "%H:%M")
    final_time = time_24hrs.replace(':', ' ')
    day_input = year + ' ' + month + ' ' + day + ' ' + final_time

    myevent_datetime = datetime.strptime(day_input, '%Y %m %d %H %M')
    
    return myevent_datetime

def main():

    year = '2023'
    month = '8'
    day = '10'
    user_time = '11:30 PM'
    #format_24hrs(year, month, day, user_time)
    
    # Delete the event
    service = get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

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
               
               #split datetime
               split_start_datetime = start_datetime.rsplit('-', 1)[0]
               print(f"summary: {event_title}")
               print(f"event start time: {split_start_datetime}")
               print(f"user time input: {format_24hrs(year, month, day, user_time).isoformat()}")
    
               if event_title == myevent_title and split_start_datetime == format_24hrs(year, month, day, user_time).isoformat():
                   event_id = event['id']
                   print("event found: " + event_id)
                   try:
                       service.events().delete(
                           calendarId='primary',
                           eventId=event_id
                       ).execute()
                       print("Event deleted.")
                   except googleapiclient.errors.HttpError:
                       print("Failed to delete event.")

    except Exception as e:
        print("error", e)
        
if __name__ == '__main__':
    main()
