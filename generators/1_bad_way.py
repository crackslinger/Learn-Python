from time import sleep

def compute():
    rv = []
    for i in range(10):
        sleep(.5)
        # this will take 10* .5 sec to process and return
        # result all at once
        rv.append(i)
    return rv

# So for us to process even a first entry we need to wait for all of them
# to get processed by some function. This could get ugly as the data gets large.
# And maybe we don't need all the data at the same time, just one by one to look at.
# So this, as we did it in this module is wasteful in terms of both time and memory.
