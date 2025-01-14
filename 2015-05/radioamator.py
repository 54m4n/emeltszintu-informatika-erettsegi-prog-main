import os

#--1--
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}veetel.txt','r')
wolf=[]
i=0
for l in f:    
    wolf.append(l)
f.close()

#--2--
print('--2--')

print(f'1. rogzites RA szama: {wolf[0].split()[1]}')
print(f'2. rogzites RA szama: {wolf[len(wolf)-2].split()[1]}')

#--3--
print('--3--')

for i in range(len(wolf)):
    if wolf[i].find("farkas")!=-1:
        print(f'nap: {wolf[i-1].split()[0]} RA szam: {wolf[i-1].split()[1]}')

#--4--
print('--4--')

rec=[]
for i in range(0,len(wolf),2):    
    rec.append(wolf[i].split())
udays=[]

for i in range(len(rec)):
    if (int(rec[i][0])) not in udays:
        udays.append(int(rec[i][0]))

udays.sort()
urecs=[]

for i in range(len(udays)):
    urecs.append(0)

for i in range(len(rec)):
    urecs[int(rec[i][0])-1]=urecs[int(rec[i][0])-1]+1

for i in range(len(udays)):
    print(f'{udays[i]}. nap: {urecs[i]} radioamator')
    
#--5--
print('--5--')
def recover(str):
    recovered=""
    message=[""]*90
    for i in range(len(str)):
        actstr="".join(str[i][0])
        for j in range(90):
            if actstr[j]!="#" and message[j]=="":
                message[j]=actstr[j]
            if actstr[j]=="#" and i==len(str)-1 and message[j]=="":
                message[j]="#"
    recovered="".join(message)
    return recovered

radio=[]

for i in range(0,len(wolf),2):    
    nap=wolf[i].split(' ')[0]
    rszam=wolf[i].split('\n')[0].split(' ')[1]
    msg=wolf[i+1].split('\n')[0]
    radio.append([nap,rszam,msg])

radio.sort(key=lambda x: x[0])

messages=[]

for i in range(len(radio)):
    index=int(radio[i][0])-1
    try:
        messages[index].append([radio[i][2]])
    except IndexError:
        messages.insert(index,[[radio[i][2]]])

for i in range(len(messages)):
    print(recover(messages[i]))

#--6--
#napok:1-11
#radioamatorok: 1-20

#n=int(input('kerem a nap szamat (1-11):'))
#r=int(input('kerem a radioamator sorszamat (1-20):'))

n=2
r=15


for i in range(len(radio)):
    if int(radio[i][0])==n and int(radio[i][1])==r:
        egyedek=radio[i][2].split(' ')[0]
        e=[]
        e.append(egyedek.split('/'))

s=0
for i in range(len(e)):
    s=s+int(e[i][0])
    s=s+int(e[i][1])

print(s)