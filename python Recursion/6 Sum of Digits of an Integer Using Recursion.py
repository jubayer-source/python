def sumofDigit(n):

    if n == 0:
        return 0
    else:
        return n % 10 + sumofDigit( n // 10)



print(sumofDigit(45))
