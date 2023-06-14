data = [i for i in range(1, 21)]
print(data)

odd = [j for j in data if j % 2 != 0]
print(odd)

even = [k for k in data if k % 2 == 0]
print(even)

greater_10 = [x for x in data if x > 10]
print(greater_10)

less_10 = [x for x in data if x <= 10]
print(less_10)
