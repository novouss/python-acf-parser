# Steam Application Cache File Parser
An ACF file is a cache file used by Valve Steam, a software package used for downloading games. It contains information related to the software and is used for the original download as well as game updates. `steamapps.py` provides the ability for python to read and parse the information inside this file. Program returns a dictionary data type of the acf file.

A pip install query will soon be added.

## Importing...
```py
import steamapps as sa
```

# Reading steamapps
```py
import steamapps as sa

# Create path to acf file
dir = "C:\\Program Files (x86)\\Steam\\steamapps\\"

# Call the 'read_dir' function
appmanifest = sa.read_dir(dir)
```

## Reading information from a directory

The first index is the appmanifest number of the game you're peering into. Then the second index is the information you wish to retrieve from the appamnifest.

```py
print(appmanifest['730']["appid"])
# Returns 730
print(appmanifest['730']["name"])
# Returns Counter-Strike: Global Offensive
print(appmanifest['730']["LauncherPath"])
# Returns C:\\\\Program Files (x86)\\\\Steam\\\\steam.exe
print(appmanifest['730']["LastUpdated"])
# Returns 1675432013
```

# Reading from a single appmanifest file
```py
import steamapps as sa

# Create path to acf file
dir = "C:\\Program Files (x86)\\Steam\\steamapps\\"
acf = 'appmanifest_730.acf'
# appmanifest_730.acf is Counter-Strike: Global Offensive and will be used as demonstration.

# Call the 'read_acf' function
appmanifest = sa.read_acf(dir + acf)
```

## Reading information from an acf file
```py
print(appmanifest["appid"])
# Returns 730
print(appmanifest["name"])
# Returns Counter-Strike: Global Offensive
print(appmanifest["LauncherPath"])
# Returns C:\\\\Program Files (x86)\\\\Steam\\\\steam.exe
print(appmanifest["LastUpdated"])
# Returns 1675432013
```
