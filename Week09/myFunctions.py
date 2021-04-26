#following along with lecture 09
#a module of useful functions
#Author: Carolyn Moorhouse
import logging

logging.basicConfig(level = logging.WARNING)

"""
function that returns the factorial number of an int
ie
7! = 7x6x5x4x3x2x1
"""

def factorial(num):
    if num <0:
        logging.warn("factorial received a number less than 0")
        return -1
    if num == 1:
        return 1
    factorial =  1
    num +=1
    for i in range(1, num):
        logging.debug("before mult %d by %d", factorial, "by", i)
        factorial *= i
        logging.debug("after mult %d", factorial)
    return factorial

if __name__ == "__main__":
   print("in My Functions", __name__)
   assert factorial(7) == 5040

#print("in My Functions")

