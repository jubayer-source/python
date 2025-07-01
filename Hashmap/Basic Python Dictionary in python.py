# Creating a hashmap (dictionary)
hashmap = {
    "apple": 3,
    "banana": 5,
    "orange": 2
}

# Accessing a value
print(hashmap["apple"])  # Output: 3

# Adding or updating a key-value pair
hashmap["grape"] = 10
hashmap["banana"] = 6
hashmap["lichi"] = 4

# Deleting a key-value pair
del hashmap["orange"]

# Checking if a key exists
if "apple" in hashmap:
    print("Apple exists.")

# Iterating through the hashmap
for key, value in hashmap.items():
    print(f"{key}: {value}")
