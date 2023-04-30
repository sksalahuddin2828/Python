print("My name GUPI, I'm  from Mars")

food = int(input("Enter Food KG: "))
print("Every days I eat 1/2 Kg food from total",food,"After that I eat another 1/2 Kg khabar from bechay thaka food thakay -- minus minus ha ha ")
stay = 0
for stay in range(food):
    food /= 2
    stay += 1
    if food <= 1:
        break
    print("Food",food,"Days",stay)
