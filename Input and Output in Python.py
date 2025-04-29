# Input and Output in Python
"""Md. Jubayer Ahmad
Jubayer Source Githup"""

name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")

#######################################
s = "Jubayer"
print(s)

########################################
s = "Jubayer_source"
age = 21
city = "Mymensingh"
print("Name: ", s,"\nAge: ",age,"\nCity:", city)

########################################
# Take Multiple Input in Python using split function

x,y = input("Enter two values: ").split()
print("Number of X number: ", x)
print("Number of Y number: ", y)

# Take now three values using split() function

a, b, c = input("Input Three values: ").split()
print("A = ",a)
print("B = ", b)
print("C = ", c)


########################################
# Take Conditional Input from user in Python

age_input = input("Enter your age: ")
age = int(age_input) # Converting the input to an integer

if age < 0:
    print("Please enter your valid age.")
elif age < 18:
    print("You are a minor")
elif age >= 18:
    print("You are and adult")
elif age >= 60:
    print("You are a senior Citizen.")
#else:
    #print("Default something")


########################################
# Print Names in Python
# Taking input as a string
name = input("What is your name ?: ")
print(name)

# convert input values as a data type like integer, float etc
age = int(input("What is your age ?: "))
print(age) # integer data
age = float(input("What is your age ?: "))
print(age) #float data


########################################
# Find DataType of Input in Python


a = "Hello world"
b = 10
c = 11.11
d = ("Greeks", "for", "Greeks")
e = ["Md.", "Jubayer", "Ahmad"]
f = {"I", "Love", "You"}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


########################################
#### Output formatting in Python

# 💡 1. Basic Decimal Formatting (Currency Style)
amount = 150.75
print("Amount: ${:.2f}".format(amount))
amount = 150.75
print(f"Amount: ${amount:.2f}")
          
          #✅# OUTPUT ###
          #Amount: $150.75
          #Amount: $150.75

# 💡 2. Padding and Alignment
amount = 160.56
print("Amount: ${:10.2f}".format(amount))
amount = 150.65
print(f"Amount: ${amount:10.2f}")
         
         ## ✅ Output:
         #Amount: $    160.56
         #Amount: $    150.65
         
#💡 3. Including Thousands Separator
amount = 123456789.67
print("Amount: ${:,.2f}".format(amount))
print(f"Amount: ${amount:,.2f}")

          #✅ Output:
          #Amount: $123,456,789.67
          #Amount: $123,456,789.67
          
#### Output formatting in Python Using sep and end parameter
# end parameter with '@'
print("Python", end='@')
print("Geeksforgeeks")

#seprating using comma
print('G', 'F', 'G', sep='-')

#formating a date
print('01', '12', '2002', sep='-')

#another example
print('Username', 'Jubayer_source', sep='@')

#### using F-string
name = 'Jubayer'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")















