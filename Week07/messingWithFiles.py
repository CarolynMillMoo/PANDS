#this program is to demonstrate file io
#following along with lecture 7
#Author: Carolyn Moorhouse

with open(".\lecture1.txt", "w") as f:
    print("create a file")

#with open("testdata.txt", "rt") as f :
    #data = f.read(2)
    #print(data)
    #for line in f:
     #   print("we got: ", line.strip())

with open("output.txt", "at") as f:
    f.write("blah the blah\n")
    print("my data", file =f)




