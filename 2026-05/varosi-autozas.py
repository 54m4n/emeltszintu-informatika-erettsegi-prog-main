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
waytmp.append([0,0,0])
for l in f:
    tmp=[]
    tmp.append(int(l.split()[0]))
    tmp.append(int(l.split()[1]))
    tmp.append(int(l.split()[2]))
    waytmp.append(tmp)


# megbasztatjuk kicsit a waytmp-t, hogy jolegyen
#   [6, 9, 3] 
#   [30, 35, 7]
#   [49, 54, 11]
#   [68, 73, 12]



way=[]
for i in range(1,len(waytmp)-120):
    t1=waytmp[i][0]
    t2=waytmp[i][1]

    vel=round((waytmp[i][2]-waytmp[i-1][2])/(waytmp[i][1]-waytmp[i][0]),2)
    dst=((waytmp[i-1][2]+waytmp[i][2])/2)*(waytmp[i][1]-waytmp[i][0])
    print(f'{waytmp[i]} -> vel: {vel} dst: {dst}')
    