from time import sleep

class Compute:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return self.last
    # there is no list so there is no storage

for val in Compute():
    print(val)
    # as we print our values they are not stored 
