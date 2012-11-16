import sys,re

if len(sys.argv) == 2:
	s =sys.argv[1]
else:
	print "USAGE: python aplist.py <file path>"
	exit()
while (s.find("/./")>0) :
	s = s.replace("/./","/")
#print s

while ( len(s) > 0  and s.find("..") > 0) :
	s = re.sub(r"/?\w+/../?","",s)
	#print s.find("..")

print s

