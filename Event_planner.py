import datetime as dt

class EventPlanner:
    def __init__(self, year):
        self.year = year
        self.events = {}
    
    def add_events(self, when, details):
        if when.date() < dt.date.today() or when.year != self.year:
            raise Exception("invalid data")
        self.events[when] = details
        
    def remove_event(self, when):
        if when in self.events:
            del self.events[when]
        else:
            raise Exception("Please check the proper Dates")
        
    def list_events(self):
        print(f"\nEvents for {self.year}:")
        for datetime, details in self.events.items():
            print(datetime.strftime('%d %B, %A, %Y, %I:%M %p'))
            print("Details:", details) 
            
year = int(input('Enter Year: '))
planner = EventPlanner(year)

for i in range(3):
    date = [int(x) for x in input('Enter Date dd/mm/yy: ').split('/')]
    time = [int(x) for x in input('Enter Time hr:min: ').split(':')]
    when = dt.datetime(date[2], date[1], date[0], time[0], time[1])
    details = input('Details of the Event: ')
    planner.add_events(when, details)

planner.list_events()
