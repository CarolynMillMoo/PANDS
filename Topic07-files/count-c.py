#a program which uses functions from "count-a.py" and "count-b.py",
#to count how many times the program has been run. Test this
#Author: Carolyn Moorhouse

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

#Main program
num = readNumber()
num += 1
print("we have run this program {} times".format(num))
writeNumber(num)

#Test= initially wasnt working as i had the "=+" with num but worked following update to correct terms


