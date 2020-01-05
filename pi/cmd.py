import os
import sys

import subprocess

import REXtools.text as TXT

#using raw strings
installPath = os.path.dirname(sys.executable)

def configUser(name, email):
    return ["git config --global user.name " + name, "git config --global user.email " + email]

def packagePath (name = ""):
    return InstallPath + r"\Lib\site-packages\"" + name

def changeDir(name):
    return "cd " + name

#github
def cloneRepo (link):
    return "git clone " + link

def commitRepo (message):
    return "git commit -m" + REXtools.str.inQuotes(message)

def pushRepo (branch = "master"):
    return "git push " + branch
def pullRepo (branch = "master"):
    #STILL GOTTA CHANGE
    return "git pull origin " + branch

def repoOrigin (link):
    return ["git remote add origin " + link, "git push -u origin master"]

#local git
def changeBranch(branch = "master"):
    return "git checkout -b " + branch
def addBranch(name = ""):
    return "git branch " + name
def addFiles (files = ["."]):
    return "git add " + REXtools.str.fromList(files, " ")

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
