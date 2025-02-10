import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--
path=os.path.dirname(__file__)

f=open(f'{path}{os.sep}src{os.sep}utasadat.txt')
utasadat=[]
for l in f:
    utasadat.append(l.strip().split())
f.close()

print(utasadat[0])

