def fizzbuzz(item):
    output = []
    for i in item:
        if i%3==0 and i%5==0:
            output.append("FizzBuzz") 
        if i%3==0:
            output.append("Fizz") 
        if i%5==0:
            output.append("Buzz") 
        else:
            output.append(str(i))
    return output
print(fizzbuzz(range(1,101)))
