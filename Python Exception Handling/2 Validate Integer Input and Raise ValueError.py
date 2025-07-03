# jubayer-source github 
# jubayer_source username for all.


def getIntegerInput(promt):

    try:
        value = int(input(promt))
        return value
    except ValueError:
        print("Error: Invalid input: Please enter a valid integer.")

n = getIntegerInput("Input a integer value: ")

print("Input Value is:", n)


# 2_Validate_Integer_Input_and_Raise_ValueError.py

def get_integer_input(prompt):
    user_input = input(prompt)
    
    if not user_input.strip().lstrip('-').isdigit():
        raise ValueError("Invalid input: Please enter a valid integer.")
    
    return int(user_input)

# Main program
try:
    number = get_integer_input("Enter an integer: ")
    print(f"You entered the integer: {number}")
except ValueError as e:
    print("Error:", e)
