import os

#--1--
print('--1--')

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}ip.txt','r')

print(f)

ip=[]

for i in f:
    ip.append(i.split())


#--2--
print('--2--')
print(f'{len(ip)}. sor van az allomanyban')

#--3--
print('--3--')

