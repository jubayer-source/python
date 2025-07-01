# jubayer-source github 

def multiply(numbers):
    total = 1
    
    for x in numbers:
        total *= x

    return total

numberList = (8, 2, 3, -1, 7)
print("Product: ", multiply(numberList))
