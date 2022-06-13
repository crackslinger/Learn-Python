from sqlite3 import connect

with connect('test.db') as conn:
    cur = conn.cursor()
    cur.execute('create table points(x int, y int)')
    cur.execute('insert into points(x, y) values(1, 1)')
    cur.execute('insert into points(x, y) values(1, 2)')
    cur.execute('insert into points(x, y) values(2, 1)')
    for row in cur.execute('select sum(x * y) from points'):
        print(row)
    cur.execute('drop table points')
