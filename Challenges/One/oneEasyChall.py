#challenge one easy, get name, age, and username. Display them
import os.path

print "What is your Name?"
name = raw_input()

print "Hold old are you?"
age = raw_input()

print "What's your user name?"
userName = raw_input()

print ("your name is " + name + ", you are " + age + " years old, and your username is " + userName)

#write it out to a file for storage later
#if file exists open it in append mode, else create it
if os.path.exists("UserData.txt"): 
	myFileOpen = open("UserData.txt","a")
else:
	myFileOpen = open("UserData.txt", "w")

#write the user info into a text file
myFileOpen.write(name+","+age+","+userName+'\n')

#close the file
myFileOpen.close()
