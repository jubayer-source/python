# Slicing
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])     # [1, 2, 3]
print(numbers[::-1])    # Reverse list

# Looping through a list
for n in numbers:
    print(n)

# List comprehension
squares = [x**2 for x in range(6)]  # [0, 1, 4, 9, 16, 25]
