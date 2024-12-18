#!/usr/bin/python
# making folders according to extensions & putting extensions to their folders respectievely

import os
import re
from sys import argv 
path=argv[1]
os.chdir(path)

def move():
    dict1={}
    for file in os.listdir():
        a=re.search(r'.*(\..+)',file)
        if a:
            if not a.group(1)[1:] in dict1.keys():
                dict1.update({a.group(1)[1:]:[file]})
            else:
                dict1[a.group(1)[1:]].append(file)


    for folder,files in dict1.items():
        if not os.path.exists(path+folder):
            os.makedirs(path+folder)
        for file in files:
            os.rename(path+file,path+folder+'/'+file)


# remove all empty dirs
def remove_empty_dirs():
    for folder in os.listdir():
        if os.path.isdir(path+folder):
            if not os.listdir(path+folder):
                os.rmdir(path+folder)

def undo():
    for folder in os.listdir():
            os.chdir(path+folder)
            for file in os.listdir():
                os.rename(path+folder+'/'+file,path+file)
            os.chdir(path)
            remove_empty_dirs() 
# move()
# undo()
while True:
    print('Would you like to move the files to their respective extensions folders:\n1.Move\n2.Undo\n3.End')
    a=input().casefold()
    if a=='end':
        break
    move() if a=='move' else undo()
