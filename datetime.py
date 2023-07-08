import datetime

# Using now() to get current time
current_time = datetime.datetime.now()

# Printing attributes of now()
print("The attributes of now() are:")
print("Year:", current_time.year)
print("Month:", current_time.month)
print("Day:", current_time.day)
print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)
print("Microsecond:", current_time.microsecond)
print("Millisecond:", current_time.microsecond // 1000)  # Convert microsecond to millisecond
print("Time Zone:", current_time.astimezone().tzinfo)

# Additional time information
print("\nAdditional time information:")
print("Weekday (Monday is 0 and Sunday is 6):", current_time.weekday())
print("Day of the year:", current_time.timetuple().tm_yday)
print("Daylight Saving Time (DST):", current_time.dst())

# Time formatting
print("\nFormatted time:")
print("ISO 8601 format:", current_time.isoformat())
print("Formatted date and time:", current_time.strftime("%Y-%m-%d %H:%M:%S.%f"))
