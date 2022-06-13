from sqlite3 import connect

# this already exists and can be imported as library
# this code can be hardcoded sepcifically for temptable, but this is reusable
class contextmanager:
    def __init__(self, gen):
        self.gen = gen
    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self
    def __enter__(self):
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)
    def __exit__(self, *args):
        next(self.gen_inst, None)

# this is generetor funct, it's useful because __enter__ and __exit___ 
# provide us some sequencing (always called in the same order).
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    yield
    cur.execute('drop table points')
temptable = contextmanager(temptable)   # here we initialize which generator to use
# we can do this initialization above generator using decorator @contexmanager

# this is how we use ctx manager "connect" from lib sqlite3
# "with" automatically implements __enter__ / __exit__ protocol
with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):    # here it would be contextmanager instead of temptable
        # if contextmanager class was written exclusively for temptable
        cur.execute('insert into points(x, y) values(1, 1)')
        cur.execute('insert into points(x, y) values(1, 2)')
        cur.execute('insert into points(x, y) values(2, 1)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)
