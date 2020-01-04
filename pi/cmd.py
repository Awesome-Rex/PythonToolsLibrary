import os
import sys
import REXtools.str

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

def run(command):
    #subprocesses
    #test comment
    pass
def runAll (commands):
    for x in commands:
        run(x)
