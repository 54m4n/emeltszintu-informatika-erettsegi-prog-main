import os

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}ip.txt','r')

print(f)

ip=[]

for i in f:
    ip.append(i.split())

print(ip[0])