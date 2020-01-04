line = "\n"
tab = "\t"
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
    return string + space
def lrS (string):
    return space + string + space

def deSpace (string):
    newString = string
    while newString[-1] == space:
        newString = newString[0:-1]

    return newString

def unEsc (string):
    newString = ""
    
    for x in string:
        if x == r"\"":
            newString += r"\""
        else:
            newString += x

    return newString

def fromList (ls, gap, l = False, r = False):
    newString = ""
    
    if l:
        newString = gap
    
    for x in ls:
        newString += x + gap

    if not r:
        newString = newString[0:-len(gap)]

    return newString
def toList (string, gap, r = False, l = False):
    ls = []
    testString = string

    scope = len(testString)
    n = 0
    
    while n < scope:
        if testString[n:n+len(gap)] == gap:
            ls.append(testString[0:n])
            testString = testString[n+len(gap):len(testString)]
            n = 0
            scope = len(testString)

            print (testString)
        elif n == scope-1:
            ls.append(testString)
            testString = ""
            n = 0
            scope = 0
        else:
            n += 1
    return ls
