#First draft, still a little hacky

import random
#Array for advanced programming students

advPro = ["mary", "jane", "sue"]

#Array for non advanced programming students

begPro = ["frank", "joe", "bob"]

#Array for non programming students

nonPro = ["sally", "jinx", "nasus", "holly"]

#Array for tables

tables = [""] * 20

#randomize all 3 student arrays

random.shuffle(begPro)
random.shuffle(advPro)
random.shuffle(nonPro)

#combine 3 arrays into 1 large array

fullList = advPro + begPro + nonPro

#calculate number of tables required based on size of array. 5 people per table
i = 1
numOfTables = len(fullList)
for x in xrange(1,20):
	if numOfTables > 5:
		numOfTables = numOfTables - 5
		i = i + 1

#Distribute the students over the tables, add 1 to each table and loop through the tables. 
for y in xrange(0,len(fullList)):
	tables[y%5] = tables[y%5] + "," + fullList[y]
#Print to screen or write to file the list of people and their given table number.
for z in xrange(0,20):
	print(z)
	print(tables[z])
