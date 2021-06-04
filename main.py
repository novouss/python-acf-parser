# Importing the class file
from steamfile import steamfile
import os

# Create path to acf file
directory = os.path.dirname(os.path.realpath(__file__))
acf_dir = directory + '\\appmanifest_730.acf'

# Initialize steamfile() and use method load()
# load() would return a dict data type of the acf file
acf = steamfile()
acf_gamefile = acf.load(acf_dir)

print(acf_gamefile)