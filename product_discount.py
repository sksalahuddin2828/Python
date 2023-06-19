def convert(amount, dis):
    convert = (amount*dis)/100           # Only 20% calculation 550 Taka
    result = convert-amount              # Now total amount is 2750 - 550 discount amount is answer
    return result                        # return result value


print(convert(2750,20))
#print(convert(100,20))
