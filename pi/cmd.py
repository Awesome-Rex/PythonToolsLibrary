import os
import sys

import subprocess

import REXtools.text as TXT

#using raw strings
installPath = os.path.dirname(sys.executable)

def packagePath (name = ""):
    return InstallPath + r"\Lib\site-packages\"" + name

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
