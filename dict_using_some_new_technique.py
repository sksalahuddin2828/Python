valuse = ('a1', 'b2', 'c3')

print(dict(valuse))

# Answer: {'a': '1', 'b': '2', 'c': '3'}

valuse = ('a1', 'b2', 'c')  # if 1 charecter is missing

print(dict(valuse))

# Answer: ERROR!
#         ValueError: dictionary update sequence element #2 has length 1; 2 is required

#--------------------------------------------------------------------------------------

# It's actually return a tuples

# valuse = ('a1', 'b2', 'c3')
# (('a': '1'), ('b': '2'), ('c': '3'))
# print(dict(valuse))
