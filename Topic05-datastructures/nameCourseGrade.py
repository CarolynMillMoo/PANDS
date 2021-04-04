#this program stores a students name and
#lists of her courses and grades in a dictionary
#the program then prints out the data
#Author: Carolyn Moorhouse

student = {
    "name" : "Mary",
    "modules" : [
        {
            "courseName" : "Programming",
            "grade" : 45
        },
        {
            "courseName" : "History",
            "grade" : 99
        }
    ]
}
print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))
    