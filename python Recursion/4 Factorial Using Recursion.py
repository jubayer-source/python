def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(999)) # max 999 number we can factorial
