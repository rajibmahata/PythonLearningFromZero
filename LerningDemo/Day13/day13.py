import datetime

# Get the current date and time
now = datetime.datetime.now()
print("Current Date & Time:", now)

# Get the current date
today = datetime.date.today()
print("Today's Date:", today)

# Create a custom date
custom_date = datetime.date(2023, 5, 17)
print("Custom Date:", custom_date)

# Time manipulation
custom_time = datetime.time(14, 30, 15)  # Hours, Minutes, Seconds
print("Custom Time:", custom_time)
