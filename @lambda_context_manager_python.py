@lambda _: _()
def func() -> str:
    print('func() was called!')
    return 'some value'

# Answer: func() was called!

#-------------------------------------------------------------------------------------------------
# Here I never call / invoke a function, I call as a variables. Carefully look in -->  print(func)

@lambda _: _()
def func() -> str:
    print('func() was called!')
    return 'some value'
    
print(func)

# Answer: func() was called!
#         some value
