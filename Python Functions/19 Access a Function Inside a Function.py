# jubayer-source github
# jubayer_source username list

 
def test(a):
    
    def add(b):
        nonlocal a # Tells Python to use 'a' from the outer scope, not local
        
        a += 1
        
        return a + b
    return add

func = test(4)   # 'a' is set to 4
print(func(4))   # 'a' becomes 5, b is 4, so result is 5 + 4 = 9

###########################
print() # one line skip
###########################


def outer_function():
    print("This is the outer function.")
    
    def inner_function():
        print("This is the inner function.")
    
    # Call the inner function from within the outer function
    inner_function()

# Call the outer function
outer_function()

