def int_to_base(n, base):

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if n < base:
        return digits[n]
    
    else:
        return int_to_base(n// base, base) + digits[n % base]
    
    
print(int_to_base(255, 2))    # Binary -> '11111111'
print(int_to_base(255, 8))    # Octal  -> '377'
print(int_to_base(255, 16))   # Hex    -> 'FF'
print(int_to_base(255, 5))    # Base 5 -> '2010'
