from optparse import OptionParser
from collections import Counter
import sys

#String array for printing end result

total = []

#String array for parsing the file for raw error messages

errors = []

#Add options

usage = "usage: %prog [options] inputfile [outputfile]"
o = OptionParser(usage=usage)
o.add_option("-f", "--full", action="store_true", dest="full", help="View error messages untruncated")
o.add_option("-o", "--output", action="store_true", dest="output", help="Write output to file")
opts, args = o.parse_args()

with open(args[0], 'r') as f:

#Loop identifies lines in file containing "ERROR," splits the error message from the DTG and system information, and stores the error messages in array errors

	for line in f:

		if "ERROR" in line:

			segments = line.split('] - ')
			line = segments[1]
			line = line.replace('\n', '')
			errors.append(line)
f.close()

#Use Counter to count occurrences and sorted to sort them into a list in descending order

count = Counter(errors)
count = sorted(count.items(), key=lambda pair: pair[1], reverse=True)

for t in count:

	uniqueErrors = []
	if str(t[0]) not in uniqueErrors:
		if opts.full:
			total.append("ERROR: " + str(t[0]) + " OCCURRENCES: " + str(t[1]))
		
		else:
			total.append("ERROR: " + str(t[0])[:100] + " OCCURRENCES: " + str(t[1]))
		uniqueErrors.append(str(t[0]))

#Checks for output option and prints to user defined filename

if opts.output:
	if len(args) < 2:
		args.append(args[0]+".ERR")	
	with open(args[1], 'w') as p:
		for i in total:
			p.write(i + '\n')
	p.close()

for i in total:

	print(i)
		
