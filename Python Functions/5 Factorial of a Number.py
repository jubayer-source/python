# jubayer-source github 

####### Recursive Approach

def facto(num):
    if num < 0:
        return "Factorial not defined for negative numbers"
    if num == 0 or num == 1:
        return 1
    return num * facto(num-1)

# Example
print(f"Factorial Number:", facto(5))


############ Iterative Approach
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    
    result = 1
    
    for i in range(2, n+1): #range(start, stop) // range(2, 6)  →  [2, 3, 4, 5]

        result *= i
    return result

# Example
print(factorial(100))
