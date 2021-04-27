#messing with objects- following along with lecture 10.2
#Author: Carolyn Moorhouse

class Nameofclass:
    name = ""
    last = ""
    def getfullname(self):
       return self.name + ' ' + self.last
    pass

inst = Nameofclass()
inst2 = Nameofclass()

inst.name = 'carolyn'
inst2.last = 'moorhouse'

person = inst
print(person.name)

inst.last = "bloks"
print(person.getfullname())

str1 = "blah de blah"
str2 = str1

str1 += " with bells on top"

print(str2)