import re
fname = raw_input('Enter a file name: ')
try:
	fhandle = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
exp = raw_input('Enter a regular expression: ')
count = 0
for line in fhandle:
	line = line.rstrip()
	query = re.findall(exp, line)
	if len(query) > 0:
		count = count + 1

print fname, 'had', count, 'lines that matched', exp