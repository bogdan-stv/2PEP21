"""
Create 2 decorators that will get applied to the function below
1) first decorator applied insures that input arguments and output values are converted to the arguments provided as decorator
2) second decorator will write each output values on a new line in a file that matches the function name
Use functions created by you
"""

from functools import wraps

def check_args(*args1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args = list(args)
            for i in range(len(args)):
                if type(args[i]) != args1[i]:
                    args[i] = args1[i](args[i])
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

def write_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open(f"{func.__name__}.txt", 'w') as file:
            for arg in args:
                file.write(f"{arg}\n")
        result = func(*args, **kwargs)
        return result
    return wrapper

@check_args(str, str)
@write_args
def function(arg1, arg2):
    print(arg1, arg2)

function("Hello", "World")

