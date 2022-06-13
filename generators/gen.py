# gen.py

# useful for interleaving of a code and enforcing sequencing
# managing memory consumption

# say we want to go through csv file and count rows
"""
csv_gen = csv_reader("some_csv.txt")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")
"""

# code below can cause Memory error if the file is too large
"""
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
"""

# solution would be to use generator function
# this version opens a file, loops through each line and yealds each row
# instead of returning it
def csv_reader(file_name):
    for ro in open(file_name, "r"):
        yield row

# generator expression or generator comprehension
csv_gen = (row for row in open(file_name))

