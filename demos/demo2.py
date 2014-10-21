""" Set the "detektor_signature" on an object.

Uses the file 'demo_files/donny/helloworldplus.py' which looks like this:

    import os

    def add(a, b):
        return a + b

    print 'Hello %s!' % 'world'
    a = 1
    print '%s + %s equals %s' % (a, a, add(a, a))

Prints misc info.
"""
import os
import detektor


class Assignment(object):
    filepath = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'demo_files', 'donny', 'helloworldplus.py'))



a = Assignment()
detektor.set_detektor_signature('python', a, 'filepath')

print 'File signature:'
print a.detektor_signature
