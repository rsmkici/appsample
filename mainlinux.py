import sys
import yaml
from yaml.loader import SafeLoader
import os
from pathlib import Path

# Findifstring checks the argument to accept only string arguments
def findifstring():
    try:
        a = int(sys.argv[1])
    except ValueError:
        a = str(sys.argv[1])
        return a
    else:
        print("please enter a string value")
        raise SystemExit

#searchbyarg checks if the nuclei-template passed by argument exists in folder
def searchbyarg(a):
    templatespath = os.getcwd()+'/'+'templates'
    filtername=str(a)
    print(os.getcwd())
    count=0
    for files in Path(templatespath).rglob('*.*'):
       splittedfilename= str(files).split('/templates/',2)
       ret = str(splittedfilename[1]).__eq__(filtername)
       if(ret):
        print("The file located at "+ files)
        return(str(files))
        ++count
    if (count==0):
      print("no file found")

#determinetheseverity checks the severity of the vulnerability
def determinetheseverity(files):
   try:
       with open(files) as f: data = yaml.load(f, Loader=SafeLoader)
   except TypeError:
       print("please check the name of the yaml file")
   else:
    dictinfo = (data.get('info'))
    print("Severity" + ":" + dictinfo.get('severity'))

new = findifstring()
files=searchbyarg(new)
determinetheseverity(files)