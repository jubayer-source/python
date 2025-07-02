# jubayer-source github
# jubayer_source username list


def perfectNumber(n):
    
    sum = 0
    
    for x in range( 1, n):
        if n % x == 0:
            sum += x
    
    return sum == n

number = 12
print(perfectNumber(number))
