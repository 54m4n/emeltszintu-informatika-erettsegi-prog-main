import os
import sys

#os.system('cls') #if it is win
os.system('clear') #if it is unix

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}naplo.txt')
l=f.read().split('# ')
f.close()

print(l[1].split('\n'))
