import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')
    
#--1--
path=os.path.dirname(__file__)

f=open(f'{path}{os.sep}src{os.sep}jeladas.txt')
autok=[]
for l in f:
    autok.append(l.split())
f.close()

#--2--
print('--2--')
print(f'utso jeladas:\nrendszam:{autok[len(autok)-1][0]}, {autok[len(autok)-1][1]}:{autok[len(autok)-1][2]}')

#--3--
print('--3--')

elso=autok[0][0]
print(f'elso auto: {elso}, jeladasok:')
for i in range(len(autok)):
    if autok[i][0]==elso:
        print(f'{autok[i][1]}:{autok[i][2]}',end=' ')
        
#--4--
print('--4--')

h=6
m=54

i=0

while int(autok[i][1])==h and int(autok[i][2])!=m:
    i=i+1

c=0
while int(autok[i][1])==h and int(autok[i][2])==m:
    c=c+1
    i=i+1

print(f'az alabbi idopontban: {h}:{m} ennyi meres volt: {c}')

#--5--
print('--5--')
max=int(autok[0][3])

maxseb=[]

for i in range(len(autok)):
    if int(autok[i][3])>max:
        maxseb=[]
        max=int(autok[i][3])
        maxseb.append(autok[i][0])
    elif int(autok[i][3])==max:
        maxseb.append(autok[i][0])
    
print(f'max mert sebesseg: {max} km/h, ezek az autok mentek ennyivel: {maxseb}')

#--6--
print('--6--')

def secbe(h,m):
    return h*3600+m*60

rszam="ZVJ-638"
szakasz=[]

for i in range(len(autok)):
    if autok[i][0]==rszam:
        szakasz.append(autok[i])
        
print(szakasz[0])
print(szakasz[1])
print(szakasz[2])
print(szakasz[3])
print('------------')

starttime=secbe(int(szakasz[0][1]),int(szakasz[0][2]))
deltasec=0
megtett=0

for i in range(1,len(szakasz)+1):    
    deltasec=abs(starttime-secbe(int(szakasz[i-1][1]),int(szakasz[i-1][2])))
    #print(f'deltasec: {deltasec} km/h: {int(szakasz[i-1][3])}')
    megtett=megtett+(int(szakasz[i-1][3])/3600)*deltasec
    print(szakasz[i-1],round(megtett,1))
    starttime=secbe(int(szakasz[i-1][1]),int(szakasz[i-1][2]))



a=(round((119/3600)*(13*60),1))
b=(round((119/3600)*(6*60),1))
print(a)
print(b)
print(a+b)