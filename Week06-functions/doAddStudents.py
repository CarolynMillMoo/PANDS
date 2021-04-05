#this prgram is to be used to read in students details
#Author: Carolyn Moorhouse

students = []
def readModules ():
    return []

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name: ")
    currentStudent["modules"]= readModules ()

    students.append(currentStudent)

#test
doAdd(students)

doAdd(students)
print(students)


