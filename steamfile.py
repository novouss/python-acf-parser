import argparse
import os

class steamfile:

    def load(self, filename):
        # Raise an Error if a non-acf file was used.
        if not filename.endswith(".acf"):
            raise argparse.ArgumentTypeError('Incorrect File Type!')
            
        with open(filename, 'r') as file:
            # Clean filename from newline and tablines
            content = [line.replace('\t\t',"") for line in file]
            content = [line.strip('\t\n') for line in content]
            # Receives index 0 of tuple because _load returns an index number
            return self.__load__(content, 0)[0]
    
    def __load__(self, content, index):
        appstate = {}
        i = index

        while i < len(content):
            x = content[i]

            # Skipping appstate index
            # Skip if we're currently in a curly brace
            if x == '"AppState"' or x == '{' or x == '}':
                i = i + 1
                continue

            line = x.split('"')

            # Skip and check if the next index is a opening curly brace
            if content[i + 1] == '{':
                appstate[line[1]], i = self.__load__(content, i + 1)
                i = i + 1
                continue

            elif content[i+1] == '}':
                appstate[line[1]] = line[3]
                return appstate, i
            
            appstate[line[1]] = line[3]
            i = i + 1
          
        return appstate, i
