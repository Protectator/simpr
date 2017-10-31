from subprocess import call
import sys
import os
import json
import shutil

# Allow to use with python 3
if (sys.version_info > (3, 0)):
	raw_input = input

# Path to script
scriptPath = os.path.realpath(__file__)
scriptFolder, scriptFile = os.path.split(scriptPath)

# Input prefix
inPrefix = "\n> "

# Client name and folder
while (True):
	clientName = raw_input('Client ?' + inPrefix)
	clientFolder = os.path.join(scriptFolder, clientName)
	if os.path.exists(clientFolder):
		break
	wannaCreateFolder = raw_input('Client "' + clientName + '" unknown. Create new ? [y]: yes, n: no' + inPrefix)
	if wannaCreateFolder == "":
		wannaCreateFolder = "y"
	if wannaCreateFolder == "y":
		os.mkdir(clientFolder)
		break
os.chdir(clientFolder)

# Project name and main folder
while (True):
	projectName = raw_input('Project Name ?' + inPrefix)
	projectFolder = os.path.join(clientFolder, projectName)
	if not os.path.exists(projectFolder):
		break
	print('Project %s alredy exists in %s.\n' % (projectName, clientName))
os.mkdir(projectFolder)
os.chdir(projectFolder)

# Folders structure
folders = ["Builds", "Assets", "Docs"]
for folderName in folders:
	os.mkdir(folderName)

# Git
gitParam = raw_input('Git ? [n]: no, i: init, c: clone' + inPrefix)
if gitParam == "":
	gitParam = "n"

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
	gitAddress = raw_input('Link to git address to clone ?' + inPrefix)
	call(["git", "clone", gitAddress, gitFolder])
	
# No git
elif gitParam == "n":
	os.mkdir("Sources")
	alreadySources = False

print('Project %s created in %s.\n' % (projectName, clientName))
