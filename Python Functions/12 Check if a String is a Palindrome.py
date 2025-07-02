# jubayer-source github
# jubayer_source username list


def Palindrome(str):
    
    s = ""
    for char in str:
        s = char + s
    
    return s == str

print(Palindrome("hello"))

###### To Remove Space  between to word ,,, and case sentive remove

def PalindromeCheck(s):
    ss = s.replace(" ", "").lower()
    return ss == ss[::-1]

print(PalindromeCheck("nurses run"))  # Output: True
