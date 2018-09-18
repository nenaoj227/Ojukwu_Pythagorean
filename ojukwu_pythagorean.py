x = raw_input ("What is your name?")
print ("Welcome, " + x)
from math import sqrt

#Defining variables and taking input from user

A = raw_input ("Enter 1st slide:")
B = raw_input ("Enter 2nd slide:")

#
ASQU = int(A) * int(A)
BSQU = int(B) * int(B)
AandB = int(ASQU)+int(BSQU)
answer = sqrt(AandB)
print "The length of side C is" + str(answer)