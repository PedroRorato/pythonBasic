from datetime import date
from datetime import time
from datetime import datetime

def main():

    # Date
    today = date.today()
    print("Today's date is", today)
    # print("Date components: ", today.day, today.month, today.year)
    # print("Today's week day number is: ", today.weekday())
    # days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    # print("Which is a: ", days[today.weekday()])

    #Datetime
    # today = datetime.now()
    # print("The current date and time is ", today)

    today = datetime.date(datetime.now())
    print("The current date and time is ", today)


if __name__ == "__main__":
    main()