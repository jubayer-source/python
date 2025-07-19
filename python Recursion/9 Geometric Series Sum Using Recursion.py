# jubayer-source github

def geometric_sum(n):
    #base case
    if n == 0:
      return 1
    
    else:
      return 1 / ( 2 ** n) + geometric_sum(n-1)

print(geometric_sum(14))
    
