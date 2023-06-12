# ASCII value converter - Ord() and Chr() Functions
# chr(interger value)
# ord(string)

x = chr(65)
print(type(x),x)

# Answer = <class 'str'> A

x = ord('A')
print(type(x),x)

# Answer = <class 'int'> 65

#---------------More ~ Example-----------------


ascii_value = 65
print(chr(ascii_value))

ascii_value = 66
print(chr(ascii_value))

ascii_value = 97
print(chr(ascii_value))

ascii_value = 35
print(chr(ascii_value))

ascii_value = 126
print(chr(ascii_value))

ascii_value = 127  
print(chr(ascii_value))  # DEL is not print in your console -- it's print BLANK

ascii_value = 'A'
print(ord(ascii_value))

ascii_value = 'B'
print(ord(ascii_value))

ascii_value = 'a'
print(ord(ascii_value))

ascii_value = 'f'
print(ord(ascii_value))

ascii_value = 'z'
print(ord(ascii_value))
