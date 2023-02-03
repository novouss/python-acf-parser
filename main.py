# Importing the class file
from steamfile import steamfile
import os

# Process a directory of ACF files
directory = "C://Program Files (x86)//Steam//steamapps//"
for filename in os.listdir(directory):
    if filename.endswith(".acf"):
        print("Processing file: " + filename)
        acf = steamfile()
        acf_gamefile = acf.load(directory+filename)
        print("Game: " + acf_gamefile["name"] + " (" + acf_gamefile["appid"] + ")")


# directory = os.path.dirname(os.path.realpath(__file__))
# acf_dir = directory + '\\appmanifest_730.acf'

# Initialize steamfile() and use method load()
# load() would return a dict data type of the acf file
# acf = steamfile()
# acf_gamefile = acf.load(acf_dir)

# print(acf_gamefile)