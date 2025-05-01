"""
Md. Jubayer Ahmad
Jubayer_source Github profile

"""

a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:",a-b)
print("Multification:", a*b)
print("Division:",a/b)
print("Floor Division:",a//b)
print("\n") # for New line

### Comparison of Python Operators
# Comparison Operators

a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b) # comparison operator return True or False value
print(a >= b)
print(a <= b)
print("\n") # For gap line


### Logical Operators in Python
"""
The precedence of Logical Operators in Python is as follows:

Logical not
logical and
logical or
"""


a = True
b = False
print(a and b)
print( a or b)
print( not a)
print("\n") # for New line

### Bitwise Operators in Python
"""
Bitwise Operators in Python are as follows:

Bitwise NOT
Bitwise Shift
Bitwise AND
Bitwise XOR
Bitwise OR
"""
# Example of Bitwize operators in Pythons

a = 10
b = 4

print(a & b) # and
print( a | b) # or -> binary add
print( ~a ) # not => -(a + 1)
print( a ^ b) # xor
print( a >> 2) # left shift   a(10) / 4 (integer division) = 2
print( a << 2) # right shift   a(10) * 4 = 40
print("\n") # for New line


### Assignment Operators in Python
a = 10
b = a

print(b)

b += a
print(b)

b -= a
print(b)

b *= a
print(b)

b <<= a
print(b)    #  b = b << a = 100 * 2^10
print("\n") # for New line


### Identity Operators in Python
a = 10
b = 20
c = a

print(a is not b) # it return True False value
print(a is c)

### Membership Operators in Python
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
    
print("\n") #for new line


### Ternary Operator in Python
# Syntax: [On_true] if [expression] else [on_false]

a, b = 10, 20
min = a if a < b else b
max = a if a > b else b

print("Minimum:",min)
print("Maximum:",max)
print("\n")
### Operator Precedence in Python

expr = 10 + 10 * 20
print(expr)
name = "Monir Bai"
age = 0

if name == "Monir Bai" or name == "Jubayer" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

print("\n")

### Operator Associativity in Python
print("Operator Associativity in Python")
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2+3))
print(2 ** 3 ** 2)
