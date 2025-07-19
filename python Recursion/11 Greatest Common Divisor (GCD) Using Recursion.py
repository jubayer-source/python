def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print("GCD(48, 36):", gcd(48, 36))
print("GCD(36, 48):", gcd(36, 48))
