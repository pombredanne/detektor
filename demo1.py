""" Get detektor signature for code in a given file.

Opens the file 'demo_files/donny/helloworldplus.py' and sends this to the
detektor codeparser.

The file looks like this:

    import os

    def add(a, b):
        return a + b

    print 'Hello %s!' % 'world'
    a = 1
    print '%s + %s equals %s' % (a, a, add(a, a))

Prints misc info.
"""
import os
import pprint
import detektor

filepath = os.path.abspath('./demo_files/donny/helloworldplus.py')

print 'Get signature for file "{}"'.format(filepath)
code_signature = detektor.get_detektor_signature_from_file(filepath)

print 'Returned code signature:'
pprint.pprint(code_signature)
