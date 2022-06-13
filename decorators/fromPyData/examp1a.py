# dec.py
from time import time

def add(x, y=10):
    return x+y

before = time()
print('add(10)',        add(10))
after = time()
print("time taken: ", after - before)
before = time()
print('add(20, 30)',    add(20, 30))
after = time()
print("time taken: ", after - before)
before = time()
print('add("a", "b")',  add("a", "b"))
after = time()
print("time taken: ", after - before)
