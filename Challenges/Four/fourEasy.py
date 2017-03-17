#Create a password generator
from random import randint

print "How long would you like your passwords?" 
length = int(raw_input())

print "How many passwords would you like?" 
amount = int(raw_input())


for amountCounter in range(1, amount+1):
	temp_pass = ''
	for lengthCounter in range(1, length+1):
		temp_pass += chr(randint(33,125))
	print temp_pass

