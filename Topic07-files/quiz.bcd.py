#the with statement will automatically close the file
#when it is finished with it

with open("test-d.txt", "w") as f:
    data = f.write("test d\n") 
    print(data)

with open ("test-b.txt", "a") as f2:
    data = f2.write("another line\n")
    print(data)

#Answer b. - "7" and "13" are returned when the program is run
#Answer c. "Another line" as it is in "w" or write mode
#answer d. "test d" and "another line" is appended to test-b.text as the file is in append mode rather than write
