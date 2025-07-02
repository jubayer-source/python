# jubayer-source github 
# jubayer_source username for all.

def testPrime(n):

    if(n==1):
        return False
    
    elif (n == 2):
        return True
    
    else:
        for x in range(2,n):

            if(n % x == 0):
                return False
        
        return True
    
print(f"Print the prime number:",testPrime(7))

#######################################  
print() # for one line gap
######       Another Approach    ##########


def primeCheck(num):

    if num <= 1:
        return False
    for i in range(2, int(num*0.5) + 1):
        if (num % i == 0 ):
            return False
    return True

print(primeCheck(7))   # True (7 is prime)
print(primeCheck(10))  # False (10 is not prime)
print(primeCheck(1))   # False (1 is not prime)

num = 12
result = primeCheck(num)

if result:
    print(result, f"The prime number is: {num}")
else:
    print(result, f"{num} is not a prime number.")
