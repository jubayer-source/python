# jubayer-source github profile

def harmonic_sum(n):
    #base case
    if n < 2:
      return 1
    else:
      return 1 / n + harmonic_sum(n-1)

print(harmonic_sum(14))
    
