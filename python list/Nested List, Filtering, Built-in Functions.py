
# Nested list
matrix = [
    [1, 2],
    [3, 4]
]
print(matrix[1][0])  # Second row (index 1) er first element = 3


flat = [item for row in matrix for item in row]
print(flat)              # Nested list ke flat kore: [1, 2, 3, 4]

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)      # 0 theke 9 porjonto shob even number


# Using built-in functions
nums = [3, 7, 1, 5]
print(sum(nums))      # 16
print(min(nums))      # 1
print(sorted(nums))   # [1, 3, 5, 7]
