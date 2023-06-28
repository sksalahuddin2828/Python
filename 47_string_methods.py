# 1: Capitalize()

_txt: str = "hELlo"
txt_: str = "heLLO"

print(_txt.capitalize())
print(txt_.capitalize())

# Answer: Hello
# Answer: Hello

#-------------------------------------

# 2: Casefold()

_txt: str = "hELlo"
txt_: str = "heLLO"

print(_txt.casefold())
print(txt_.casefold())

# Answer: hello
# Answer: hello

#-------------------------------------

# 3: Center()

txt_: str = "Hello, World!"
_txt: str = "Hello, World!"

print(txt_.center(20))
print(_txt.center(20, "."))
print(_txt.center(20, "-"))
print(_txt.center(20, "_"))

# Answer:    Hello, World!
# Answer: ...Hello, World!....
# Answer: ---Hello, World!----
# Answer: ___Hello, World!____

#-------------------------------------

# 4: Count()

_txt: str = "abc_abc_abc_abc"

print(_txt.count("bc"))

# Answer: 4

#-------------------------------------

# 5: Endswith()

_txt: str = "apple"

print(_txt.endswith("e"))
print(_txt.endswith(("e", "a")))   # Tuple formate inside

# Answer: True
# Answer: True


# 5: Endswith()

_txt: str = "appla"

print(_txt.endswith(("e", "a")))   # Tuple formate inside checking more charecter

# Answer: True


# 5: Endswith()

_txt: str = "applz"

print(_txt.endswith(("e", "a")))  # Tuple formate inside checking more charecter, But when it's check 'z' in the last charecter, it's give False result.

# Answer: False

#-------------------------------------

# 6: Expandtabs()

_txt: str = "first_tab\tsecond_tab\tthird_tab"

print(_txt.expandtabs(20))

# Answer: first_tab           second_tab          third_tab

#-------------------------------------

# 7: Find()

_txt: str = "Remember to Follow in GitHub!"

possition: int = _txt.find("GitHub")
print(possition)
print(_txt[possition:])

# Answer: 22          # It's locate at index 22
# Answer: GitHub!

#-------------------------------------

# 8: Formate()

_txt: str = "Potka {subject} is doing: {action}."
print(_txt.format(subject="cat", action="meow"))

# Answer: Potka cat is doing: meow.

# Alternative way:
_txt: str = "Potka {} is doing: {}."
print(_txt.format("cat", "meow"))

# Answer: Potka cat is doing: meow.

#-------------------------------------

# 9: Format_Map()

points: dict = {"First": 10, "Second": -5}
_txt: str = "Points: ({First}, {Second})"
print(_txt.format_map(points))

# Answer: Points: (10, -5)

#-------------------------------------

# 10: Index()

_txt: str = "Remember to Follow me in GitHub!"

possition: int = _txt.index("Follow")
print(possition)
print(_txt[possition:])

# Answer: 12          
# Answer: Follow me in GitHub!

#-------------------------------------

# 11: IsAlNum()

_txt: str = "helloRaya123"
txt_: str = "helloRaya123!"   # Because here are 'exclamation = !' mark symbol. ( False )

print(_txt.isalnum())
print(txt_.isalnum())

# Answer: True
# Answer: False

#-------------------------------------

# 12: IsAscii()

_txt: str = "helloRaya123"
txt_: str = "helloRaya123©"    # Because here are 'copyright = ©' mark symbol. ( False )

print(_txt.isascii())
print(txt_.isascii())

# Answer: True
# Answer: False

#-------------------------------------

# But isdecimal() can not work with "" isdigit() and isnumeric() ""
# If a string is a decimal, it also a degit and numeric
# 13: IsDecimal()

_txt: str = "123"
txt_: str = "Aa123"

print(_txt.isdecimal())
print(txt_.isdecimal())

# Answer: True
# Answer: False

#-------------------------------------

# Numeric can also work with isdecimal() 

# If a string is a digit, then it is also numeric
# 14: IsDigit()

txt_: str = "123"
_txt: str = "①②③④⑤⑥⑦⑧⑨"                # Note that these bubble characters are numeric.
_txt_: str = "一二三四五六七八九十"      # This Japanese character number is numeric, it won't work on isdigit().

print(txt_.isdigit())
print(_txt.isdigit())
print(_txt_.isdigit())

# Answer: True
# Answer: True
# Answer: False

#-------------------------------------

# Numeric can also work with isdecimal() and isdigit()

# 15: IsNumeric()

_txt_: str = "123"
txt_: str = "①②③④⑤⑥⑦⑧⑨" 
_txt: str = "一二三四五六七八九十"        # This Japanese character number is numeric number.

print(_txt_.isnumeric())
print(txt_.isnumeric())
print(_txt.isnumeric())

# Answer: True
# Answer: True
# Answer: True

#-------------------------------------

# 16: IsIdentifier()  # variable name check, if it's valid

_txt: str = "_name"        
txt_: str = "test_name"
_txt_: str = "123name"

print(_txt.isidentifier())
print(txt_.isidentifier())
print(_txt_.isidentifier())

# Answer: True
# Answer: True
# Answer: False

#-------------------------------------

# 17: IsPrintable()

_txt: str = "Hello World\n" 
txt_: str = "Hello World" 

print(_txt.isprintable())
print(txt_.isprintable())

# Answer: False
# Answer: True

#-------------------------------------

# 17: IsLower()

_txt: str = "Hello World!" 
txt_: str = "hello world!" 

print(_txt.islower())
print(txt_.islower())

# Answer: False
# Answer: True

#-------------------------------------

# 18: IsUpper()

_txt: str = "HELLO WORLD!" 
txt_: str = "hello world!" 

print(_txt.isupper())
print(txt_.isupper())

# Answer: True
# Answer: False

#-------------------------------------

# 19: IsSpace()

_txt: str = "     "

print(_txt.isspace())

# Answer: True

_txt: str = "A    "

print(_txt.isspace())

# Answer: False

#-------------------------------------

# 20: IsTitle()

txt_: str = "This Is Title"

print(txt_.istitle())

# Answer: True

_txt: str = "This is title"

print(_txt.istitle())

# Answer: False

#-------------------------------------

# 21: Join()

txt: str = '-'

print(txt.join(['text1', 'text2', 'text3']))

# Answer: text1-text2-text3


# Alternative way:

print('-'.join(['text1', 'text2', 'text3']))

# Answer: text1-text2-text3

#-------------------------------------

# 22: LJust()

txt: str = 'hello'
_txt: str = 'world'

print(txt.ljust(20, '_'))
print(_txt.ljust(20, '-'))

# Answer: hello_______________
# Answer: world---------------

#-------------------------------------

# 23: Lower()

txt: str = 'HELLO, WORLD!'

print(txt.lower())

# Answer: hello, world!

#-------------------------------------

# 24: Upper()

txt: str = 'hello, world!'

print(txt.upper())

# Answer: HELLO, WORLD!

#-------------------------------------

# 25: LStrip()

txt: str = 'Hello World.'

print(txt.lstrip('Hello'))

# Answer: World.

#-------------------------------------

# 26: Maketrans() 
# and
# 27: Translate()

txt: str = 'This is Banana'
table = txt.maketrans('a', '😊')

print(table)                      # ASCII table small a value is 'a' = 97 charecter it's change to 'smile emoji' charecter to '😊' = 128522
print(txt.translate(table))

# Answer: {97: 128522}
#         This is B😊n😊n😊

#-------------------------------------

# 28: Partition()

txt: str = 'a+b=c'

print(txt.partition('='))

# Answer: ('a+b', '=', 'c')

#-------------------------------------

# 29: RemovePrefix()

txt: str = 'Google Apps'

print(txt.removeprefix('Google'))
print(txt.removeprefix('Google').strip())  # Using strip() functions or methods to remove white space from (left and right) both side

# Answer:  Apps
# Answer: Apps

#-------------------------------------

# 30: RemoveSuffix()

txt: str = 'Google Apps'

print(txt.removesuffix('Apps'))

# Answer: Google

#-------------------------------------

# 31: Replace()

txt: str = 'Remember to Follow.'
print(txt.replace('Remember', 'Subscribe'))

# Answer: Subscribe to Follow.

txt: str = 'Remember to Follow, & Follow.'
print(txt.replace('Follow', 'Subscribe', 1))

# Answer: Remember to Subscribe, & Follow.

#-------------------------------------

# 32: Find()   # find() use for the first elements
# and
# 33: RFind()  # rfind() use for the last elements

txt: str = 'A: Some text. A'
print(txt.find('A')) 

# Answer: 0


txt: str = 'A: Some text. A'
print(txt.rfind('A')) 

# Answer: 14

# if don't find anything the gives answer negative one or -1 both
txt: str = 'A: Some text. A'
print(txt.find('A')) 
print(txt.rfind('A')) 

# Answer: -1
# Answer: -1

#-------------------------------------

# 34: RIndex()

txt: str = 'A: Some text. A'
print(txt.rindex('A')) 

# Answer: 14

txt: str = 'A: Some text. A'
print(txt.rindex('B'))       # if not found, raises error

# Answer: substring not found

#-------------------------------------

# 35: RJust()

txt: str = 'Good'

print(txt.rjust(20, '_')) 

# Answer: ________________Good

#-------------------------------------

# 36: rpartition()

txt: str = 'text1=text2=text3'
print(txt.rpartition('=')) 

# Answer: ('text1=text2', '=', 'text3')

txt: str = 'text1=text2=text3'
print(txt.partition('=')) 

# Answer: ('text1', '=', 'text2=text3')

#-------------------------------------

# 37: split()
# and
# 38: rsplit()

txt: str = 'This is some special character.'
print(txt.rsplit(sep=' ')) 

# Answer: ['This', 'is', 'some', 'special', 'character.']

txt: str = 'https://www.example.com/'
print(txt.rsplit(sep='.')) 

# Answer: ['https://www', 'example', 'com/']

txt: str = 'This is some special character.'
print(txt.split(maxsplit=2)) 

# Answer: ['This', 'is', 'some special character.']

#-------------------------------------

# 39: RStrip()

txt: str = 'Her name is Raya Raya'  
print(txt.rstrip('Raya'))           

# Answer: Her name is Raya         # last one 'Raya' is remove

#-------------------------------------

# 40: splitlines()

txt: str = "Remember to Follow!\nor else...\n"
print(txt.splitlines(keepends=True)) 

# Answer: ['Remember to Follow!\n', 'or else...\n']

txt: str = "Remember to Follow!\nor else...\n"
print(txt.splitlines()) 

# Answer: ['Remember to Follow!', 'or else...']

#-------------------------------------

# 41: startswith()

txt: str = "Anupama Dey Raya"
print(txt.startswith('A')) 

# Answer: True

txt: str = "Anupama Dey Raya"
print(txt.startswith('R')) 

# Answer: False

#-------------------------------------

# 42: strip()

txt: str = "Anupama Dey Ray"
print(txt.strip("Anupama")) 

# Answer: Dey Ray

txt: str = "Anupama Dey Ray"
print(txt.strip("Ray")) 

# Answer: Anupama Dey 

#-------------------------------------

# 43: swapcase()

txt: str = "Anupama Dey Ray"
print(txt.swapcase()) 

# Answer: aNUPAMA dEY rAY

#-------------------------------------

# 44: title()

txt: str = "this is a title"
print(txt.title()) 

# Answer: This Is A Title

#-------------------------------------

# 45: zfill()

txt: str = 'some text'
print(txt.zfill(20))

# Answer: 00000000000some text

txt: str = '30'
print(txt.zfill(5))

# Answer: 00030

#-------------------------------------

# 46: 
