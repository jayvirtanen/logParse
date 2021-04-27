from collections import Counter
total = []
checker = []
with open("console.log") as f:
	content_list = []
	for line in f:
		if "ERROR" in line:
			line.rstrip()
			segments = line.split('] - ')
			line = segments[1]
			line = line.replace('\n', '') 
			content_list.append(line)
count = Counter(content_list)
for i in count.elements():
	if i not in checker:
		checker.append(i)
		total.append("ERROR " + i +" appears in logs " + str(count[i]) + " times")
for i in total:
	print(i)

