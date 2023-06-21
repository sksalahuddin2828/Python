# Prime Number using range() function in a function

number = range(0,1000)

def prime_num(number):
    for i in range(2,number):
        if number % 2 == 0:
            return False
        return True

# Watch it via Tuple:
prime_number = tuple(filter(prime_num, num))
print(prime_number)


# Watch it via List:
# prime_number = list(filter(prime_num, num))  
# print(prime_number)
