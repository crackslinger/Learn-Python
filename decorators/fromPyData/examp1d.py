# will introduce decorators here
from time import time

# we're making timer funct which takes as an arg another function(add, sub)
# and we're wrapping it w/ some behavior defined in yet another funct
# so every time sub or add is called their wrapper function gets called
def timer(func):
    def f(*args, **kwargs):     # change hardcoded perimeters
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('elapsed', after - before)
        return rv
    return f

@timer
def add(x, y=10):
    return x + y
# add = timer(add)  # python made this easier w/ decorator

@timer
def sub(x, y=10):
    return x - y
# sub = timer(sub)  # @timer above function is equivalent to this line of code


print('add(10)',        add(10))
print('add(20, 30)',    add(20, 30))
print('add("a", "b")',  add("a", "b"))
print('sub(10)',        sub(10))
print('sub(20, 30)',    sub(20, 30))
#print('sub("a", "b")',  sub("a", "b"))  # strings do not subtract
