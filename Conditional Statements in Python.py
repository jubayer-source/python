"""''''''''''''''''''''''
Md. Jubayer Ahmad
Jubayer_source github profile

'''''''''''''''''''''''''"""

### if condition  
age = 20
if age >= 20:
    print("Eligible to Vote.")
    
# short form of if condition

if age >= 20: print("Eligible to Vote from 18")

###If else Conditional Statements in Python
age = 10
if age <=12:
    print("Travel for  free.")
else:
    print("Pay for ticket.")

#Short Hand if-else
marks = 45
res = "Pass" if marks >= 40 else "Fail" # like ternary operator of C/C++.... :?

print(f"Result: {res}")
print("Result:",res)

### elif Statement in Python
age = 25

if age <= 12:
    print("Child.")
elif age <=19:
    print("Teenager.")
elif age <=35: 
    print("Young Adult.")
    print("You are the Adult you man, Am I right?")
else: print("Adult.")

### Nested if..else Conditional Statements in Python

age = 70
is_member = True


if age >= 60:
    if is_member:
        print("30% senior discount!.")
    else:
        print("20% senior discount")
else :
    print("Not eligible for a senior discount.")
    
### Ternary Conditional Statement in Python
# Assign a value based on a condition
age = 17
s = "Adult" if age >= 18 else "Minor"
print(s)

age = 21
s = "Adult" if age >= 18 else "Minor"
print(s)

### Match-Case Statement in Python
### Switch statement

number = 3

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")