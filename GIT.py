


def configUser(name, email):
    return ["git config --global user.name " + name, "git config --global user.email " + email]


#hub
def clone (link):
    return "git clone " + link

def commit (message):
    return "git commit -m" + REXtools.str.inQuotes(message)

def push (branch = "master"):
    return "git push " + branch
def pull (branch = "master"):
    #STILL GOTTA CHANGE
    return "git pull origin " + branch

def setOrigin (link):
    return ["git remote add origin " + link, "git push -u origin master"]


#local
def changeBranch(branch = "master"):
    return "git checkout -b " + branch
def addBranch(name = ""):
    return "git branch " + name
def addFiles (files = ["."]):
    return "git add " + REXtools.str.fromList(files, " ")
