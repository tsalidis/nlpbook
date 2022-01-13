
import re

text1 = "ένα,δύο,τρία,τέσσερα,πέντε,έξι"

tokens = text1.split(",")

print(tokens)

text2 = "ένα,δύο-τρία/τέσσερα!πέντε.έξι"
 
tokens = re.split('[-,/.!]', text2)

print(tokens)

tokens = re.split('((?<=[-,/.!])|(?=[-,/.!]))', text2) 

print(tokens)

tokens = [tokens[i] for i in range(len(tokens)) if len(tokens[i]) > 0]

print(tokens)

