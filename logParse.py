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
o.add_option("-q", "--quiet", action="store_true", dest="quiet", help="Run program with no terminal output")
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

#Counter counts error instances, sorts them in descending order and messages are input into final array to be printed. Truncated depending on -f option

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

#prints to file if -o option used

if opts.output:

	if len(args) < 2:

		args.append(args[0]+".ERR")	

	with open(args[1], 'w') as p:

		for i in total:

			p.write(i + '\n')

	p.close()

#Prints to terminal if not quiet

if not opts.quiet:

	for i in total:

		print(i)
		
