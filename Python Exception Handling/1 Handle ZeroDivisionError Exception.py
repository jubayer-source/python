# jubayer-source github 
# jubayer_source username for all.

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example usage
num1 = 10
num2 = 0
divide_numbers(num1, num2)


# 1_Handle_ZeroDivisionError_Exception.py
def safe_division():
    while True:
        try:
            numerator = int(input("Enter the numerator: "))
            denominator = int(input("Enter the denominator: "))
            result = numerator / denominator
            print(f"Result: {numerator} / {denominator} = {result:.2f}")
            break  # Exit loop if successful
        except ZeroDivisionError:
            print("Error: You cannot divide by zero. Please try again.")
        except ValueError:
            print("Error: Please enter numeric values only.")

# Run the function
safe_division()
