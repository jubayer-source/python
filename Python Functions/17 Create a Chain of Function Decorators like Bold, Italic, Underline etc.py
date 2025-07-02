# jubayer-source github
# jubayer_source username list


def makeBold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

# define decorator for italic
def makeItalic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

# define decorator for underline
def makeUnderline(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

# Apply decorators
@makeBold
@makeItalic
@makeUnderline
def greet():
    return "Hello, world!"

# call the decorated function
print(greet())
