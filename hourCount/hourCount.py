'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour 
of the day for each of the messages. You can pull the hour out from the 'From ' line by 
finding the time and then splitting the string a second time using a colon. Example -
"From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

#Function to open the file
def openFile():
	name = raw_input("Enter file:")
	if len(name) < 1 : name = "mbox-short.txt"
	handle = open(name)
	return handle

file = openFile()
countdict = dict()

#Read through the lines, cut hours and count
for line in file:
    if not line.startswith('From '): continue
    line = line.split()
    countdict[line[5][0:2]] = countdict.get(line[5][0:2],0) + 1
    #print countdict
    
for x,y in sorted(countdict.items()):
    print x,y
                  