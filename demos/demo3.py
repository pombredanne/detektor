""" Set the "detektor_signature" on multiple objects.

This demo shows how to send multiple objects to detektor. It will add an
attribute "detektor_signature" which can be used for comparing in a later step.

Also it shows how the attribute holding the path for the file that should be analyzed can be at an arbitrary depth.

Uses the following files:

* 'demo_files/donny/helloworldplus.py'
* 'demo_files/larry/helloworldplus.py'

"""
import os
import detektor


demo_files_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'demo_files'))


class FileClass(object):
    def __init__(self, filepath):
        self.filepath = filepath


class AssignmentDonny(object):
    def __init__(self):
        self.fileclass = FileClass(
            os.path.join(demo_files_directory, 'donny', 'helloworldplus.py'))


class AssignmentLarry(object):
    def __init__(self):
        self.fileclass = FileClass(
            os.path.join(demo_files_directory, 'larry', 'helloworldplus.py'))


assignments = [
    AssignmentDonny(),
    AssignmentLarry(),
]

# You can also send multiple objects, and the path can go deeper
detektor.set_detektor_signature('python', assignments, 'fileclass.filepath')

for a in assignments:
    print 'File signature:'
    print a.detektor_signature
    print
