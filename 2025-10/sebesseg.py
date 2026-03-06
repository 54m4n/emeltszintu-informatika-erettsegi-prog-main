import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--
print('--1--')

path=os.path.dirname(__file__)

f=open(f'{path}{os.sep}src{os.sep}ut.txt')

ut=[]
c=0
for i in f:
    if c==0:
        sumroad=int(i)
    else:
        a=int(i.strip().split()[0])
        try:
            b=int(i.strip().split()[1])
        except:
            b=i.strip().split()[1]        
        ut.extend([[a,b]])
    c=c+1
f.close()

#--2--
print('--2--')

for i in range(len(ut)):
    if len(str(ut[i][1]))>=4:
        print(ut[i][1])

#--3--
print('--3--')
minseb=int(ut[0][1])
aktseb=0
vizsgal=33930
#faszom konyorogjon a juzernek bazmeg inputert ..|..

i=0
c=0

while c<len(ut) and int(ut[i][0])<=vizsgal:    
    if ut[i][1]=="#" or ut[i][1]=="%" or len(str(ut[i][1]))>=4:
        pass
    elif ut[i][1]=="]":
        aktseb=90
    else:
        aktseb=int(ut[i][1])
    if int(aktseb)<=int(minseb):
        minseb=aktseb
    c=c+1
    i=i+1

print(f'A(z) {ut[0][1]}-{ut[c][0]} szakaszon a legkisebb megengedett sebesseg: {minseb}km/h')


#--4--
print('--4--')

f=0
t=0
tmp=0

iscity=False
cway=0

for i in range(len(ut)):       
    if len(str(ut[i][1]))<4 and iscity==True:
        cway=cway+(ut[i-1][0]-ut[i][0])
    if len(str(ut[i][1]))>=4:
        iscity=True
    if isinstance(ut[i][1],int)==False and str(ut[i][1][0])==']':
        iscity=False

print(f'Az ut {round(abs(cway)/(sumroad/100),2)}%-a vezet telepulesen.')
        

#--5--
print('--5--')

city="Varos301"

i=0

while i<=len(ut)-1 and ut[i][1]!=city:
    i=i+1

j=i
c=0
tol=ut[j][0]

while ut[j][1]!="]":
    if (isinstance(ut[j][1],int))==True:
        c=c+1

    j=j+1
    ig=ut[j][0]

print(f'Az alabbi utszakaszon: {tol}-{ig} osszessen {c}db jelzotabla volt.')