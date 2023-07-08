import datetime
from tabulate import tabulate

# Define the number of years to display
num_years = 5

# Create an empty table
table = []

# Get the current year
current_year = datetime.datetime.now().year

# Iterate over the years
for year in range(current_year, current_year + num_years):
    # Get the current time for each year
    current_time = datetime.datetime.now().replace(year=year)
    
    # Append the time attributes to the table
    table.append([
        year,
        current_time.month,
        current_time.day,
        current_time.hour,
        current_time.minute,
        current_time.second,
        current_time.microsecond,
        current_time.microsecond // 1000,
        str(current_time.astimezone().tzinfo)
    ])

# Display the table
headers = ["Year", "Month", "Day", "Hour", "Minute", "Second", "Microsecond", "Millisecond", "Time Zone"]
print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
# print(tabulate(table, headers=headers"))
