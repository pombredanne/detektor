import os
import logging

# Set base path
DETEKTOR = os.path.dirname(__file__)

os.environ.update({'DETEKTOR': DETEKTOR})

# Setting DEBUG = True means you'll have to read loads of output
DEBUG = True  
# Setting VERBOSE = True means you'll have to read even more output
VERBOSE = True

DEBUG = False

loglevel = 'INFO'
if DEBUG:
    loglevel = 'DEBUG'
logging.basicConfig(level=loglevel)

