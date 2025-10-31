# A decorator in Python is a function that modifies another function
# It allows you to add extra behavior without changing the original function’s code

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        result = func(*args, **kwargs)
        print("After the function runs")
        return result
    return wrapper


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles 🍬")
        result = func(*args, **kwargs)
        print("Sprinkles added ✅")
        return result
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge 🍫")
        result = func(*args, **kwargs)
        print("Fudge added ✅")
        return result
    return wrapper


@decorator
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b


# When stacking decorators, the bottom one runs first.
@add_sprinkles
@add_fudge
def get_ice_cream(flavor="vanilla"):
    print(f"Here is your {flavor} ice cream 🍦")


# Test the functions
get_ice_cream("chocolate")
print()
print("Result:", add(5, 3))
