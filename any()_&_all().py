any_true = any([False, False, True])

all_true = all([True, True, True])

print("Any:", any_true)
print("All:", all_true)
print("")

any_true = any([False, False, True])

all_true = all([False, True, True])

print("Any:", any_true)
print("All:", all_true)
print("")



numbers = [-1, -2, -4, 0, 3, -7]

# Manually looping
has_positives = False 

for n in numbers:
  if n > 0:
    has_positives = True 
    break 

# Refactor using any()
# Compression syntax 
has_positives = any(n > 0 for n in numbers)

print("Looping Any:",has_positives)
print("")
# Answer: True 



numbers = [-1, -2, -4, 0, 3, -7]

# Manually looping
has_positives = False 

for n in numbers:
  if n > 0:
    has_positives = True 
    break 

# Refactor using any()
# Compression syntax 
has_positives = all(n > 0 for n in numbers)

print("Looping All:",has_positives)
# Answer: False 
