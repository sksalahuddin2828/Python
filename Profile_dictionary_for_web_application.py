# User information for web application to store our profile dictionary

profile = {
    # Default values
    "Name" : "N/A",
    "Email" : "N/A",
    "Phone" : "N/A"
}

# it store data from user_input dictionary to profile dictionary

user_input = {
    "Name" : "Sk. Salahuddin",
    "Phone" : "+88011223344556677"
}

# Union operator only available on Python 3.9 or above

profile |= user_input

# profile.update(user_input)
# profile = {**profile, **user_input}

print(profile)