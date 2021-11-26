# import date from datetime
from datetime import date
from datetime import time
from datetime import datetime

def main():
    #get today date
    today = date.today()
    print("Today ",today)

    #print date's individual componnent
    print("date componenents: ", today.day, today.month, today.year)

    #retreive today's weekday number (Monday:0 Sunday:6)
    print("Today's weekday number is ", today.weekday())
    days = ["mon","tue","wed","thu","fri","sat","sun"]
    print("which is ",days[today.weekday()])

    #getting date and time
    today = datetime.now()
    print("current date and time: ", today)

    #time now
    t = datetime.time(datetime.now())
    print("current time: ", t)

if __name__ == "__main__":
    main()