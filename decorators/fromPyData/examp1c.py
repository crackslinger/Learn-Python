from time import time

def timer(func, x, y):
    before = time()
    rv = func(x, y)
    after = time()
    print('elapsed', after - before)
    return rv


def add(x, y=10):
    return x + y

def sub(x, y=10):
    return x - y


print('add(10)',        timer(add, 10))
print('add(20, 30)',    timer(add, 20, 30))
print('add("a", "b")',  timer(add, "a", "b"))
print('sub(10)',        timer(sub, 10))
print('sub(20, 30)',    timer(sub, 20, 30))
print('sub("a", "b")',  timer(sub, "a", "b"))
