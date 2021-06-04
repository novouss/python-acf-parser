# Steam Application Cace File Parser
An ACF file is a cache file used by Valve Steam, a software package used for downloading games. It contains information related to the software and is used for the original download as well as game updates. `steamfile.py` provides the ability for python to read and parse the information inside this file. Program returns a dictionary data type of the acf file.

## Importing...
```py
from steamfile as steamfile
```

## How to use...
```py
import os 

# Create path to acf file
directory = os.path.dirname(os.path.realpath(__file__))
acf_dir = directory + '\\appmanifest_730.acf' 
# appmanifest_730.acf is Counter-Strike: Global Offensive and will be used as demonstration.

# Initialize steamfile() and use method load()
# load() would return a dict data type of the acf file
acf = steamfile()
acf_gamefile = acf.load(acf_dir)
```

## Retrieving game information
```py
print(acf_gamefile["appid"])
# Returns 730
print(acf_gamefile["name"])
# Returns Counter-Strike: Global Offensive
print(acf_gamefile["installdir"])
# Returns Counter-Strike Global Offensive
print(acf_gamefile["LastUpdated"])
# Returns 7592902989
```