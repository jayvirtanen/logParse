from collections import Counter
import sys

#String array for printing end result
total = []
#String array to check against to make sure entries aren't duplicated in 'total'
checker = []
#String array for parsing the file for raw error messages
error_list = []

#Accept input file

with open(sys.argv[1], 'r') as f:

	for line in f:

		if "ERROR" in line:

			segments = line.split('] - ')

#Splits the line at the delimiter between the "extra information" and the actual error message

			line = segments[1]
			line = line.replace('\n', '')

#Removes superfluous newline character at the end of the line before being added to error list

			error_list.append(line)

#Counter creates a paired list of each error and the number of times it has occurred

count = Counter(error_list)
for i in count.elements():

#unpairs i (error message) and count[i] (occurrence number) by only passing each unique message to be appended to 'total' once

	if i not in checker:

		checker.append(i)
		total.append("ERROR: " + i[0:100] +" OCCURENCES: " + str(count[i]))

for i in total:
	print(i)

