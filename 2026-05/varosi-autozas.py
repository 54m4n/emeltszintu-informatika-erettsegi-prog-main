import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--
carid="mx234"

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}{carid}.txt')

waytmp=[]

for l in f:
    tmp=[]
    tmp.append(int(l.split()[0]))
    tmp.append(int(l.split()[1]))
    tmp.append(int(l.split()[2]))
    waytmp.append(tmp)


# megbasztatjuk kicsit a waytmp-t, hogy jolegyen
way=[]

for i in range(len(waytmp)-120):
    print(waytmp[i])