number = int(input("Please enter the total number you want to enter: "))

array = []
for i in range(number):
    element = int(input(f"Enter the element {i + 1}: "))
    array.append(element)

for i in range(number // 2):
    temp = array[i]
    array[i] = array[number - 1 - i]
    array[number - 1 - i] = temp

print("\nReverse all elements of the array:")
for element in array:
    print(element)
