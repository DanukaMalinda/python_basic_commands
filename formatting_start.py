from datetime import datetime

def main():
    #time and date can be formatted using predefined string
    #control codes
    now = datetime.now()

    #%y/%Y : year , %a/%A : Weekday , %b/%B:month , %d : day
    print(now.strftime("Current year is: %Y"))
    print(now.strftime("%a, %d %B, %y"))

    #%c - locale's date and time , %x -locale's date, %X - locale's time
    print(now.strftime("Locale's date and time : %c")) 
    print(now.strftime("Locale's date : %x")) 
    print(now.strftime("Locale's time : %X")) 

    #time formating
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locales's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24H time: %H:%M:%S"))
    
if __name__ == "__main__":
    main()