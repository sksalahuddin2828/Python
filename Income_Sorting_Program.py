income_list = []
print("Enter the income of 10 people:")
for person in range(10):
    income = int(input("Enter income: "))
    income_list.append(income)

for first_index in range(9):
    swap_count = 0
    min_income = income_list[first_index]
    for second_index in range(first_index + 1, 10):
        if min_income > income_list[second_index]:
            min_income = income_list[second_index]
            swap_count += 1
            min_index = second_index
    if swap_count != 0:
        temp = income_list[first_index]
        income_list[first_index] = min_income
        income_list[min_index] = temp

print("Sorted income list:")
print(income_list)


#----------testing-----------
# for i in range(10):
#     print(income_list[i])
