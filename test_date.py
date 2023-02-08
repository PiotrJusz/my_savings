import datetime


def current_day():

    now = datetime.datetime.now()

    current_time = now.strftime("%Y-%m-%d")
    print("Current Time =", current_time)

current_day()
