'''This program is a command line calendar that allows a user to view their calendar and add, update, and delete existing events.
This is based on a code academy project that I am trying to simplify and improve.
-The Zymurgist- Nov 2017'''

from time import sleep, strftime
USERNAME = "Zach"
EMPTY = "The calendar is empty."
calendar = {}

#display the welcome message to the user
def welcome():
  print "Welcome, " + USERNAME
  print "The calendar is opening..."
  sleep(1)
  print "Today's date is " + strftime("%A %B %d, %Y")
  print "The time is " + strftime("%H:%M:%S")
  sleep(1)
  
  print "What would you like to do?"
  
#check if calendar is empty
def is_empty(calendar):
	return True if len(calendar.keys()) < 1 else False
	 
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Type 'A' to Add, 'U' to Update, 'V' to View, 'D' to Delete, 'X' to Exit: ").upper()
    
    #view the calendar
    if user_choice == "V":
      print EMPTY if is_empty(calendar) else calendar
        
    #update the calendar
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update successful!"
      print calendar
    
    #add event to calendar
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:11]) < int(strftime("%Y")):
        print "An invalid date was entered."
        try_again = raw_input("Try again? 'Y' for Yes, 'N' for No: ").upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "The event was successfully added!"
        print calendar
    
    #delete event from calendar
    elif user_choice == "D":
      print EMPTY if is_empty(calendar)
      else:
        event = raw_input("What event?")
        for date in calendar.keys():
          if calendar[date] == event:
            del calendar[date]
            print "The event was successfully deleted!"
            print calendar
          else:
            print "No event by that description was found."
            #consider adding try again dialogue here, or creating a separate function for it
            
    #exit calendar
    elif user_choice == "X":
      print "Exiting..."
      start = False
      
    #garbage  
    else:
      print "An invalid command was entered.\nExiting..."
      start = False
      
start_calendar()