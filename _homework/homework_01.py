""" Create 2 decorators that will get applied to the function below
    1) first decorator applied insures that input arguments and output values are converted to the arguments provided as decorator
    2) second decorator will write each output values on a new line in a file that matches the function name
    Use functions created by you
"""

from functools import wraps

def greeting(*args1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(f"{func.__name__}.txt", 'w') as file:
                for arg in args1:
                    file.write(f"{arg}\n")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@greeting("Hello", "World")
def introduction(name):
    print(f"My name is {name}")

introduction("Bogdan")
