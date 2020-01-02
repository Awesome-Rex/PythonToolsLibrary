line = "\n"
space = " "

sing = "'"
doub = '"'

def inQuotes (string, single = False):
    if not single:
        return doub + string + doub
    else:
        return sing + string + sing

def lS (string):
    return space + string
def rS (string):
    return string space
def lrS (string):
    return space + string + space
