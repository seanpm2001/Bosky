#!/usr/bin/env python3.11
# Start of script
def checkSetup():
  videoSettings = bool(false) # How do I set a value in another file, and read it from here, without resetting each time?
  webcamSettings = bool(false)
  privacySettings = bool(false)
  if (videoSettings = "false"):
    setupInit = bool(false)
    break;
  elif (videoSettings = "true"):
      if (webcamSettings = "false"):
        setupInit = bool(false)
        break
      elif (webcamSettings = "true"):
        if (privacySettings = "false"):
          setupInit = bool("false")
          break
        else:
          setupInit = bool("true")
          break
print ("Welcome to Bosky\nThe modern day Boss Key software")
print ("The program is initializing")
return checkSetup()
if (setupInit == "false"):
  print ("Setup needs to continue before you can use Bosky")
  break
  if (videoSettings = "false"):
    open file "/Bosky/Video-export/VIDEO-EXPORT.cpp"
    break
  else:
    if (webcamSettings = "false"):
      open file "/Bosky/Video-export/PRIVACY-EXPORT.cpp"
      break
print ("Starting Bosky")
break

# File info
# File type: Python source file (*.py)
# File version: 1 (2021, Wednesday, November 10th at 4:39 pm)
# Line count (including blank lines and compiler line): 43

# End of script
