from time import sleep
# for infinite sequencing will have to use yield, coz momory's finite bruh
def infinite_sequencing():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequencing():
    print(i, end=" ")
