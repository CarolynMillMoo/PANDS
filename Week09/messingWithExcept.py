#this program is following along with lecture 9
#how you can use try except
#Author: Carolyn Moorhouse

#filename = 'Week09\data.txt'
import sys 

#print(sys.argv)
filename = sys.argv[0]

try:
  with open(filename) as f:
    print(f.read())
  var = 10/0
except FileNotFoundError:
    print("file does (", filename,") does not exist", sep='')


print("the end")