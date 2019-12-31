import math

Digits = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15
}

def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

def signFloor(num):
    return math.floor(abs(num)) * sign(num)

def signCeil(num):
    return math.ceil(abs(num)) * sign(num)

def GetKey (dictionary, value):
    for x in dictionary:
        if dictionary[x] == value:
            return x

#strings can have negative indexing
def convertBase(a, aBase = 10, bBase = 10):
    global Digits
    
    aDec = 0
    
    x = 1
    n = len(a) - 1
    
    while n >= 0:
        aDec += Digits[a[n].upper()] * x
        x *= aBase
        n -= 1
    
    abBase = "";
    
    while aDec / bBase >= 1:
        x = bBase
        
        while (aDec / x) >= 1:
            x *= bBase

        x /= bBase
        
        abBase = abBase + GetKey(Digits, (aDec - (aDec % x)) / x)
 
        aDec = aDec % x

    if aDec % bBase != 0:
        abBase = abBase + GetKey(Digits, aDec % bBase)
    
    return abBase
