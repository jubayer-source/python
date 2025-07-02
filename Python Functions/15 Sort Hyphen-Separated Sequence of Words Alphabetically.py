# jubayer-source github
# jubayer_source username list


def sort_hypen_sequence(sequence):
    
    words = sequence.split('-') # Split the input into a list of words
    
    words.sort()  # Sort the list alphabetically

    return '-'.join(words)

input_sequence = "green-red-yellow-black-white" # Sample input

# Print the sorted result
print(sort_hypen_sequence(input_sequence))
