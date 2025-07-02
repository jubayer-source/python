# jubayer-source github
# jubayer_source others username


def count_upper_lower(s):
    upper_count = 0
    lower_count = 0

    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print(f"No. of Upper case characters : {upper_count}")
    print(f"No. of Lower case Characters : {lower_count}")

count_upper_lower("The quick Brow Fox")

print() ## for one line skip
########################### Another approach
def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())

    print(f"No. of Upper case characters : {upper_count}")
    print(f"No. of Lower case Characters : {lower_count}")

# Example call
count_upper_lower("The quick Brow Fox")
