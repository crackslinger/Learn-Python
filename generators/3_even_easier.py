from time import sleep
# using generator syntax

# this function is generator object and it's state is maintained internally
def compute():
    for i in range(10):
        sleep(.5)
        yield i

# this prints out all of them:
#for val in compute():
#    print(val)

# iterating over vals 1 by 1 in py shell use print(x.__next__())
x = compute()
