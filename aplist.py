import sys,re

if len(sys.argv) == 2:
        s =sys.argv[1]
else:
        print "USAGE: python aplist.py <file path>"
        exit()

# a flag to indicate presence of a leading slash 
leading_slash=0

# substitute multiple consectuive occurences of / with a single /
s = re.sub(r"/+","/",s)

if (s[0]=='/') :
	leading_slash=1
	s= s[1:]
# replace all occurences of /./ with /
while (s.find("/./")>0) :
        s = s.replace("/./","/")

## store components of path in a list
comp = s.split('/')

out=[]
for item in comp:
	if(item!='..'):
		out.append(item)
	else:
		try:
			out.pop()  #when .. is encountered in list , pop the last element from list
		except IndexError:
			print "invalid"
			exit()
			
if (leading_slash ==1 ):
	print "/" + "/".join(out)
else :

	print "/".join(out)
