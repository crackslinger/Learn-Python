from time import time

def add(x, y=10):
    before = time()
    rv = x + y
    after = time()
    print('elapsed: ' after - before)
    return rv

# Still not the best situation because we now need to add
# all the time-tracking code to this function again
def sub(x, y=10):
    return x - y

print('add(10)',        add(10))
print('add(20, 30)',    add(20, 30))
print('add("a", "b")',  add("a", "b"))
print('sub(10)',        sub(10))
print('sub(20, 30)',    sub(20, 30))
print('sub("a", "b")',  sub("a", "b"))
