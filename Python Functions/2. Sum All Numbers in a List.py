# jubayer - source github 
def sumlist(numbers):
    return sum(numbers)

numberList = (1,2,3,4,5)
print("Sum:", sumlist(numberList))

##########################
# Another approach
##########################
def sum(numbers):
    total = 0
    
    for x in numbers:
        total += x

    return total

print("Summation: ", sum(numberList))
