group_of_list = [[1, 2], [3, 4]]

for i in group_of_list:
  for element in i:
    print(element)
print("")

def function(parameter: str):
  print(parameter)
  return function 

# You can add here multiple argument 
function('A')('B')('C')
