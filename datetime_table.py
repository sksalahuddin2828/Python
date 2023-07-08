import datetime
from tabulate import tabulate

# Using now() to get current time
current_time = datetime.datetime.now()

# Creating the table data
table_data = [
    ["Year", current_time.year],
    ["Month", current_time.month],
    ["Day", current_time.day],
    ["Hour", current_time.hour],
    ["Minute", current_time.minute],
    ["Second", current_time.second],
    ["Microsecond", current_time.microsecond],
    ["Millisecond", current_time.microsecond // 1000],  # Convert microsecond to millisecond
    ["Time Zone", str(current_time.astimezone().tzinfo)]
]

# Additional time information
table_data += [
    ["Weekday (Monday is 0 and Sunday is 6)", current_time.weekday()],
    ["Day of the year", current_time.timetuple().tm_yday],
    ["Daylight Saving Time (DST)", current_time.dst()]
]

# Time formatting
table_data += [
    ["ISO 8601 format", current_time.isoformat()],
    ["Formatted date and time", current_time.strftime("%Y-%m-%d %H:%M:%S.%f")]
]

# Printing the table
print(tabulate(table_data, headers=["Attribute (Phenomenon)", "Value (Epoch)"]))
