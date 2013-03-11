from sys import argv
script, filename = argv

#open file
f = open(filename)

#initialize ratings dict
ratings = {}

# read through file lines
lines = f.readlines()

#for each line, split names from ratings and add to dict
for line in lines:
	line_list = line.split(":")
	ratings[line_list[0]] = int(line_list[1])


# sort ratings by restaurant name and print result
for key, value in sorted(ratings.iteritems()):
	print "Restaurant %r is rated at %r" %(key, value)
