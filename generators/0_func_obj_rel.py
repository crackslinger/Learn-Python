# There's always some top-level syntax(function) and some underscore method that
# implements it.                x()         --------->      __call__
#                       
# Everything in python is an object represented by a class. 
# So when we code something like this:

def add1(x, y):
    return x + y

# under the hood object-model for add1 function looks something like this:
class Adder:
    def __call__(self, x, y):
        return x + y

add2 = Adder()

# which is the same thing
