"""
Do not use comparison operator " == " for password check
because this is vulnerable for timing attacks
instead you should use compare_digest from secrets 
because this is much more vulnerable for timing attack
and more cryptographically secured
"""

# Example: do not use it -->

user_input = "donotlove123"
password = "donotlove123"
print(user_input == password)

# Answer: True

#--------------Using this------------>>

from secrets import compare_digest

user_input = "donotlove123"
password = "donotlove123"

print(compare_digest(user_input, password))

# Answer: True
