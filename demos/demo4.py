import os
import sys
import glob
import detektor

demo_files_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'demo_files'))
os.chdir(demo_files_directory)
dirlist = glob.glob('*')

dirlist = [d for d in dirlist if os.path.isdir(d)]
filename = 'helloworldplus.py'


class Assignment(object):
    def __init__(self, filepath):
        self.filepath = filepath

assignments = []
for d in dirlist:
    assignment = Assignment(os.path.join(os.path.abspath(d), filename))
    assignments.append(assignment)

detektor.set_detektor_signature('python', assignments, 'filepath')
result = detektor.compare(assignments)

for compared in result:
    print '{} points:'.format(compared.get('points'))
    print compared.get('object1').filepath
    print compared.get('object2').filepath
    for d in compared.get('details'):
        print d
    print


sys.exit()
