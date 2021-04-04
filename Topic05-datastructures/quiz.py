#Lab05 Data structures quiz
#Author: Carolyn Moorhouse

numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "Joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [12, 'Fred', False, {}]
someone = dict(firstname = "Joe")
me = {
    "firstName" : "Andrew",
    "teaching" : [{
        "courseName" : "programming",
        "semester" : 1
    },{
        "courseName" : "Data Representation",
        "semester" : 2
    }
    ]
}
print (type(numberOfQuestions), "a.")
print (type(averageAge), "b.")
print (type(debugMode), "c.")
print (type(name), "d.")
print (type(ages), "e.")
print (type(months), "f.")
print (type(months[1]), "g.")
print (type(book), "h.")
print (type(stuff), "i.")
print (type(stuff[2]), "j.")
print (type(someone), "k.")
print (type(someone["firstname"]), "l.")
print (type(me), "m.")
print (type(me["teaching"]), "n.")
print (type(me["teaching"] [0] ["semester"]), "o.")
print (type(me["teaching"] [0] ["courseName"]), "p.")


