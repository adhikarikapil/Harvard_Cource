# Decoraters are mainly used to check if the user is logged in or not where the function needs the user to be logged in

def announce(func):
    # The function used now often wraps the parameter function so it is called wrapper function
    def wrapper():
        print("About to run the function...")
        func()
        print("Done with the function")

    return wrapper


# wrapping the argument funtion inside the decorater using @
@announce
def hello():
    print("Hello, World!!!")


hello()
