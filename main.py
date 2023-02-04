import steamapps as sa

# Create path to acf file
dir = "C:\\Program Files (x86)\\Steam\\steamapps\\"
acf = 'appmanifest_730.acf'
# appmanifest_730.acf is Counter-Strike: Global Offensive and will be used as demonstration.

# Call the 'read_acf' function
appmanifest = sa.read_acf(dir + acf)