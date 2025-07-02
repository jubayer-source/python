# jubayer-source github
# jubayer_source others username
def test_range(n):

    for n in range(4,8):
        return print("N is available in the range (4 to 8)")

    else:
        print("not")

test_range(5)

#########################
print() # for one line gap


def is_in_range(number, lower, upper):

    return lower <= number <= upper

print(is_in_range(5, 1, 10))  # True
print(is_in_range(0, 1, 10))  # False
print(is_in_range(10, 1, 10)) # True


########################################
print() # for one line gap

def check_range(num, low, up):

    if low <= num <= up:
        print(f"Yes, {num} is within the range {low} to {up}")
    else:
        print(f"No, {num} is not within the range{low} to {up}")

check_range(5, 1, 10)   # Yes, 5 is within the range 1 to 10.
check_range(0, 1, 10)   # No, 0 is not within the range 1 to 10.
check_range(10, 10, 20) # Yes, 10 is within the range 10 to 20.
