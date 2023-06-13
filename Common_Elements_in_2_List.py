# Python Program to find the intersection of two lists input by the users (Find common elements)

lst_1 = eval(input("Enter 1st List: "))
lst_2 = eval(input("Enter 2nd List: "))

store = []

for i in lst_1:
  for j in lst_2:
    if i == j:
      store.append(i)
      
print("Common Elements: ")
print(store)


