# wrapper function takes arbitrary positional and kw args, 
# ntimes is decorator function which for any given n 
# calls the function it's wrapped around n number of times
#n=2
def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                rv = f(*args, **kwargs)
            return rv
        return wrapper
    return inner

@ntimes(5)
def helloworld():
    return print("Hello World")

# Look up "closure practice duality"
