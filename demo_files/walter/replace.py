import re, sys

# a program for replacing all string occurences with a new string

if not len(sys.argv) == 6:
    # 5 arguments has to be sent
    print 'Usage: python replace1.py string with repl in filename'
    # exit if number of arguments is out of bounds
    sys.exit(0)



# get the arguments
old_str = sys.argv[1]
new_str = sys.argv[3]
filename = sys.argv[5]
try:
    f = open(filename, 'r')
except:
    # could not open this file
    print 'Cannot open file', filename
    sys.exit(1)

lines = f.readlines()
# loop through all lines and replace old string
for i in range(len(lines)):
    s2, sum = re.subn(old_str, new_str, lines[i])
    if sum > 0:
        lines[i] = s2

f.close() 
f = open(filename, 'w')
for line in lines:
    f.write(line) 
f.close() # save

