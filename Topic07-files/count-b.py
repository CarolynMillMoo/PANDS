#a function that takes in a number and overwrites a file with that number "count.txt"
#Author: Carolyn Moorhouse

filename = "count.txt"
def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

writeNumber(4)

#Comment: yes this worked the number in the "count.txt" is now 3