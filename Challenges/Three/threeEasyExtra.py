#simple cipher
import codecs
from sys import argv, exit

types = {
 'encrypt': lambda phrase : codecs.encode(str(phrase), 'rot_13'),
 'decrypt': lambda phrase : codecs.decode(str(phrase), 'rot_13') 
} 
if (argv[1]) not in types:
  print "Error: Wrong type: " ((argv[1]), '|'.join(types))
  exit(1) 

phrase = map(str, argv[2:])
print types[argv[1]](phrase).split("'")[1]

