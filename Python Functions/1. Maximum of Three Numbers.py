# jubayer-source github
def max_of_two(x,y):

    if x > y:
        return x
    
    return y

def max_of_three(x,y,z):
    # Call max_of_two function to find the maximum of y and z,
    # then compare it with x to find the overall maximum
    return max_of_two(x, max_of_two(y,z))


print(max_of_two(2,3)) # output 3

print(max_of_three(4,6,7)) # output 7
