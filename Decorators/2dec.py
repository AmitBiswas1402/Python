def debug(func):
    def wrapper(*args, **kwargs):
        args_val = ', '.join(str(arg) for arg in args)
        kwargs_val = ', '.join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"Calling: {func.__name__} with args {args_val} and kwargs {kwargs_val} ")
        return func(*args, **kwargs) 
                   
    return wrapper

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")
   
greet("Namaskaaram", greeting="Pranipaat")