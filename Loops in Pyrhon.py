#########################################
# Md. Jubayer Ahmad                     #
# Jubayer_source github profile         #
#########################################

from __future__ import print_function


# While Loop in Python
cnt = 0
while( cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")
print("\n")

# Using else statement with While Loop in Python
count = 0
while (count < 3):
    print("Hello Geek")
    count += 1
else:
    print("In Else Block")
print("\n")

# Infinite While Loop in Python

"""count = 0
while (count == 0):
    print("Hello Geek")"""
print("\n")

### For Loop in Python
n =  4
for i in range(0, n):
    print(i)

print("\n")


print("Example with List, Tuple, String, and Dictionary")
print("Iteration Using for Loops in Python")

lists = ["Md.", "Jubayer", "Ahmad"]
for i in lists:
    print(i)

print("\n")

tuples = ("Geeks", "for", "geeks")
for i in tuples:
    print(i)

print("\n")


s = "Geeks"
for i in s:
    print(i)
print("\n")

d = dict({'x': 123, 'y':354})
for i in d:
    print("%s %d" % (i, d[i]))
print("\n")

set1 = {1, 3, 5, 7, 9}
for i in set1:
    print(i)
print("\n")

print("Iterating by the Index of Sequences")

list = ["Md.", "Jubayer", "Ahmad"]
for index in range(len(list)):
    print(list[index])


print("Using else Statement with for Loop in Python")
list = ["Md.", "Jubayer", "Ahmad"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")

print("\nNested Loops in Python")


#########################################
# from __future__ import print_function #
#########################################
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
    
### Loop Control Statements
print("\nContinue Statement  :")
for letter in 'Geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter:', letter)

print('\nBreak statement in python')
# Break statement in python
for letter in 'Geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
    print('Current Letter:', letter)
    
print("\nPass Statement")
for letter in 'geeksforgeeks':
    pass
print('Last Letter:', letter)


