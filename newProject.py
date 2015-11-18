from subprocess import call
import os
import json
import shutil

# Path to script
scriptPath = os.path.realpath(__file__)
scriptFolder, scriptFile = os.path.split(scriptPath)

# Input prefix
inPrefix = "> "

# Client name and folder
clientName = raw_input('Client ?\n' + inPrefix)
clientFolder = os.path.join(scriptFolder, clientName)
if not os.path.exists(clientFolder):
	os.mkdir(clientFolder)
os.chdir(clientFolder)

# Project name and main folder
projectName = raw_input('Project Name ?\n' + inPrefix)

projectFolder = os.path.join(clientFolder, projectName)
os.mkdir(projectFolder)
os.chdir(projectFolder)

# Folders structure
folders = ["Builds", "Assets", "Docs"]
for folderName in folders:
	os.mkdir(folderName)

# Git
gitParam = raw_input('Git ? n: no, i: init, c: clone\n' + inPrefix)

# Git init
if gitParam == "i":
	alreadySources = False
	os.mkdir("Sources")
	os.chdir("Sources")
	gitFolder = os.path.join(projectFolder, "Sources")
	call(["git", "init"])
	
# Git clone
elif gitParam == "c":
	alreadySources = True
	gitFolder = os.path.join(projectFolder, "Sources")
	gitAddress = raw_input('Link to git address to clone ?\n' + inPrefix)
	call(["git", "clone", gitAddress, gitFolder])
	
# No git
elif gitParam == "n":
	os.mkdir("Sources")
	alreadySources = False

print('Project %s created in %s.' % (projectName, clientName))