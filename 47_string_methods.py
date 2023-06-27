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
