#############################################################
###### A script that replaces strings in a given file  ######
#############################################################

import sys, re # Import needed modules

# Check that right arguments have been supplied,
# or exit with message
if not len(sys.argv) == 4:
    print 'Wrong number of arguments'
    sys.exit(1)
replace     = sys.argv[1]
replacement = sys.argv[2]
infile      = sys.argv[3]

# Try to read the file to replace strings in, and
# exit if that could not be done
try:
    ifile = open(infile, 'r')
except:
    print 'Cannot open file', infile
    sys.exit(1)

# Get all lines from file into a list, and replace the
# strings found in it
linelist = ifile.readlines()
for lineno in range(len(linelist)):
    # uses a tmp var for string
    tmp_line,sum = re.subn(replace,replacement,linelist[lineno])
    # and replaces only if a replacement was done
    if sum > 0: linelist[lineno] = tmp_line
ifile.close() # close the file
outfile = open(infile, 'w') # Open the file for writing
for l in linelist: outfile.write(l) 
# Save the file with replacements
outfile.close()

#############################################################
#############################################################

