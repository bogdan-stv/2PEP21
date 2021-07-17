from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        if wrapper.calls <= 5:
            result = func(*args, **kwargs)
            return result
        else:
            raise RuntimeError("The function was executed more than 5 times")
    wrapper.calls = 0

    return wrapper

@decorator
def function():
    print("does nothing")

for _ in range(6):
    function()
    print(function.calls)