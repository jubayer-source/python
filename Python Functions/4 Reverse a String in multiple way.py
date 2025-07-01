# jubayer-source github 

def reverse_String(string):
    return string[::-1]

# sample usage
sample_string = "1234abcde"
print("Reversed:", reverse_String(sample_string))


#########################################
def string_reverse(str1):

    reversedString = ''

    index = len(str1)

    while index > 0:
        reversedString += str1[index - 1]

        index = index - 1
    
    return reversedString

print(string_reverse('12345abcade'))

###### Manual method (Using a loop )
def revString(s):
    rev_string = ''
    
    for c in s:
        rev_string = c + rev_string  # c + rev_string & rev_string + c is not same.. one is pre add another is post adding..
    return rev_string

# Example
print(revString("1234abcd"))  # Output: dcba4321
