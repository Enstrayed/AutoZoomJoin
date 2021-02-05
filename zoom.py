#      Automatic Zoom Join Script
#  Created by ctaetcsh in January 2021

#  This code is considered INCOMPLETE and should only be
#  used as reference or as a base to complete the project.

#       Copyright (C) 2021 Nathan M. [ctaetcsh]
#  This code is licened under the BSD 3-Clause License


#      -=- Important Message (Please Read) -=-
#  This file (zoom.py) is joined with a file (zoom.json)
#  which contains the links used in recursive functions
#  in this script. As this JSON file contained restricted
#  links, the file has been cleared and replaced with filler.


# Import cool stuff 😎
from win10toast import ToastNotifier
from datetime import date
import webbrowser
import json
import time
import os, signal

# init stuff
toaster = ToastNotifier()
zoomUrlArray = ["https://ctaetcsh.xyz/oops.html"] #! This array must start with something so that the numbered selections match up with the array.
printOutCounter = 0                               #! This could easilly be worked around by having the openJoinURL func look for "NOTALLOWED" and
                                                  #! reject to open the URL.

# create functions
def sendNotif(title,msg): #! This functions whole purpose is because im too lazy to type line 34 each time.
    toaster.show_toast(title, msg, threaded=True, icon_path=None, duration=3)

def openJoinURL(reqClass):
    sendNotif("Opening a URL",jsonData["classes"][reqClass]["zoomUrl"]) #! Tells user that a link is being opened.
    webbrowser.open(jsonData["classes"][reqClass]["zoomUrl"])           #! Link is opened in default web browser.

    
# Import zoom.json
with open('zoom.json') as f:
    jsonData = json.load(f)  #! Opens zoom.json file. SCRIPT AND JSON MUST BE IN SAME DIRECTORY!

os.system("cls") #! Clear screen

for x in jsonData["classes"]:  #! Recursive function to print information from classes part of JSON
    zoomUrlArray.append(x)

for x in jsonData["classes"]:
    if jsonData["classes"][x]["timeHour"] > 12:
        listTimeHour = jsonData["classes"][x]["timeHour"] - 12
    else:
        listTimeHour = listTimeHour = jsonData["classes"][x]["timeHour"]

    if "timeMin" in jsonData["classes"][x]:
        listTimeMin = jsonData["classes"][x]["timeMin"]
    else:
        listTimeMin = "00"

    printOutCounter = printOutCounter + 1

    print("["+str(printOutCounter)+"] "+jsonData["classes"][x]["class"]+" at "+str(listTimeHour)+":"+str(listTimeMin))


#!  Seen below: Work in progress attempt to kill zoom when class is over.

# This worked to kill etcher!
#os.kill(248, signal.SIGTERM)
#os.kill(17216, signal.SIGTERM)
#os.kill(19160, signal.SIGTERM)
#os.kill(17248, signal.SIGTERM)



#Enter your selection as an int, then run openJoinURL
openJoinURL(zoomUrlArray[int(input("Please your selection: "))])
