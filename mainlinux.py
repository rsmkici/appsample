import sys
import yaml
from yaml.loader import SafeLoader
import os
from pathlib import Path


def findifstring():
    try:
        a = int(sys.argv[1])
    except ValueError:
        a = str(sys.argv[1])
        return a
    else:
        print("please enter a string value")
        raise SystemExit


def searchbyarg(a):
    os.mkdir('/usr/src/app/applocal/appsample/')
    os.chdir('/usr/src/app/applocal/appsample/')
    templatespath = os.getcwd()+'/'+'templates'
    filtername=str(a)
    print(os.getcwd())
    print('Get current file name :', __file__)
    print('get filename'+ (templatespath))
    count=0
    for files in Path(templatespath).rglob('*.*'):
       splittedfilename= str(files).split('/templates/',2)
       print(splittedfilename[1])
       ret = str(splittedfilename[1]).__eq__(filtername)
       if(ret):
        print(splittedfilename[1])
        print(files)
        return(str(files))
        ++count
    if (count==0):
      print("no file found")

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