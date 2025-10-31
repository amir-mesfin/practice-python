# A decorator in Python is a function that modifies another function —
# it lets you add extra behavior without changing the original function’s code
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles")
        func(*args, **kwargs)
        print("Sprinkles added")
    return wrapper
def add_funge(fun):
    def warraper(*args, **kwargs):
        print("Adding funge")
        fun(*args, **kwargs)
        print("funge added")
    return warraper

@add_sprinkles
@add_funge
def get_ice_cream(flavor="vanilla"):
    print(f" hear is your ice cream flavord {flavor} ")


get_ice_cream("chocolate")
