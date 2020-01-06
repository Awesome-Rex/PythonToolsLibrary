import os
import sys

import subprocess

import REXtools.text as TXT

#using raw strings
installPath = os.path.dirname(sys.executable)

packagePaths = {
"win" : r"\Lib\sit-packages\"",
"pi" : {"single" : r"~\.local\lib\python",
        "system" : r"\usr\local\lib\python",
        "apt" : r"\usr\lib\python"}
}
def packagePath (os, version = 3, name = ""):
    return os + str(version) + "\\" + name

def changeDir(name):
    return "cd " + name

def run(command, SHELL=False):
    #can also do run(stdout=subprocess.PIPE, text=True).stdout

    #.stdout    output
    #.stderr    error
    #.returncode    boolean success
    if SHELL:
        return subprocess.run(command, capture_output=True, text=True, shell=True)
    else:
        return subprocess.run(TXT.toList(command, " "), capture_output=True, text=True)
def runAll (commands):
    returns = []
    for x in commands:
        returns.append(run(x))

    return returns
