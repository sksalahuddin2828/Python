# Using Unicode character this "\u0332" print underline

def under_line(text):
    print("\u0332".join(text))
    print("\u0332".join("Python Programming"))
    
under_line("Sk. Salahuddin")

# ------------------------------------------------------

def line():
    for i in range(1,15):
        print("_",end="")            # You can use underscore _ , Hash # , etc = print("#",end="")
    print()
print("Sk. Salahuddin")
line()
print("Python Programming")
line()
