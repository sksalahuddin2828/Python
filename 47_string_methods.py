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

