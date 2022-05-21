""" Building a basic command line calendar using python 2 """

from time import sleep,strftime
user_firstname=input("Enter your firstname: ")
calendar={}
def welcome():
  print ("Welcome "+user_firstname)
  print ("Calendar is starting")
  sleep(1)
  print ("Today's Date: "+strftime("%A %B %d %Y"))
  print ("Current time: "+strftime("%H:%M:%S"))
  sleep(1)
  print ("What would you like to do?")
def start_calendar():
  welcome()
  start=True
  while start:
    user_choice= input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit:")
    user_choice=user_choice.upper()
    if user_choice=="V":
      if(len(calendar.keys())<1):
        print("Calendar is empty")
      else:
        print (calendar)
    elif user_choice=="U":
      date=input("What date? ")
      update=input("Enter the update: ")
      calendar[date]=update
      print("Update is successful")
    elif user_choice=="A":
      event=input("Enter Event: ")
      date=input("Enter date (MM/DD/YYYY): ")
      if (len(date)>10 or int(date[6:])>int(strftime("%Y"))):
        print("Invalid date was entered")
        try_again=input("Try Again? Y for Yes, N for No: ")
        try_again=try_again.upper()
        if try_again=="Y":
          continue
        else:
          start=False
      else:
        calendar[date]=event
        print("Event was successfully added")
    elif user_choice=="D":
      if (len(calendar.keys())<1):
        print ("Calendar is empty")
      else:
        event=input("What event?")
        for date in calendar.keys():
          if event==calendar[date]:
            del calendar[date]
            print ("Event was successfully deleted")
            print (calendar)
          else:
            print ("Incorrect event was specified")
    else:
        print("Invalid command was entered")
        start=False
start_calendar()