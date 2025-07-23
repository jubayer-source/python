# Unpacking
a, b, *rest = [10, 20, 30, 40]
print(a)      # 10
print(rest)   # [30, 40]

# Spread operator
list1 = [1, 2]
list2 = [3, 4]
combined = [*list1, *list2]  # [1, 2, 3, 4]
