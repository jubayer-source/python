# jubayer_source

def sum_series(n):
    #base case
    if n <= 0:
      return 0
    else:
      return n + sum_series(n - 2)

print(sum_series(124))
    
