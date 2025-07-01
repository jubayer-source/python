text = "apple banana apple orange banana apple"

#initialize empty hashmap 
word_count = {}

# Split text into words and count frequencies
for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# print the word frequencies
print(word_count)

# iterating through the hashmap
for key, value in word_count.items():
     print(f"{key} : {value}")
