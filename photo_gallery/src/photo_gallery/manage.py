#!/usr/bin/python
from django.core.management import execute_manager
from os.path import abspath, dirname, curdir
import sys

base_dir = dirname(dirname(abspath(__file__)))
gallery = dirname(abspath(curdir)) + "/gallery"


sys.path.insert(0,base_dir)
#print "Updating Path with: %s" % (base_dir)
sys.path.insert(0,gallery)    

try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
