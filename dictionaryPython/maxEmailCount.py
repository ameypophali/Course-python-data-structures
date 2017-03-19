'''
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
#Function to get the filename
def getFileName():
    name = raw_input("Enter file:")	
    
    if len(name)<1: 
        print "Wrong name provided"
        exit(1)
    else:
	handle = open(name)
    
	return handle 

#Get the file name
file = getFileName()
count = 0 
countDict = dict()

#Populate the dictionary with Email and counts
for line in file:
    if line.startswith('From '):
        line = line.split()
        countDict[line[1]] = countDict.get(line[1],0)+1
    else:
    	continue

#Get the highest count
biggestVal = 0
biggestKey = None
for key,val in countDict.items():
    if(val>biggestVal):
        biggestVal = val
        biggestKey = key

print biggestKey,biggestVal
	


