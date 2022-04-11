##############################################
# Intro
# corncob_caps.txt sourced from http://www.mieliestronk.com/wordlist.html
#
##############################################

# Read in text file
print("Using readlines()")

Letters = ["{REDACTED}"] 
goodlist = []

with open("corncob_caps.txt") as file:
    for item in file:
        if len(item) == 6:
            #print("##################")
            #print("Outer good")
            goodlist.append(item) 

print("Sample")            
print(goodlist[:10])

print("Size")
print(len(goodlist))

newlist = []
for item in goodlist:
        if "{REDACTED}" in item:
            newlist.append(item) 

print("Sample")            
print(newlist[10:])

print("Size")
print(len(newlist))

sort3 = []
for item in newlist:
        if "{REDACTED}" in item:
            sort3.append(item) 

print("Sample")            
print(sort3[10:])

print("Size")
print(len(sort3))

sort4 = []
for item in sort3:
        if "{REDACTED}" in item:
            sort4.append(item) 

print("Sample")            
print(sort4[10:])

print("Size")
print(len(sort4))

