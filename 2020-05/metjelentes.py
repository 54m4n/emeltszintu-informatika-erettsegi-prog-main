import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}tavirathu13.txt')

met=[]

for l in f:
    telepules=l.strip().split()[0]
    hm=l.strip().split()[1][0:4:1]
    i=l.strip().split()[2][0:3:1]
    e=l.strip().split()[2][3:5:1]
    c=int(l.strip().split()[3])
    met.append([telepules,hm,i,e,c])
        
f.close()

print(met[0])

#--2--
print('--2--')

i=len(met)-1
t="SM"

while i>=0 or met[i][0]!=t:
    i=i-1
print(f'Az alabbi telepulesrol: {met[i][0]} utoljara {met[i][1]}:{met[i][2]}-kor erkezett adat.')

#--3--
print('--3--')
min=int(met[0][4])
max=int(met[0][4])
maxindex=0
minindex=0


for i in range(len(met)):
    if int(met[i][4])>max:        
        max=int(met[i][4])
        maxindex=i
    if int(met[i][4])<min:        
        min=int(met[i][4])
        minindex=i
    


print(f'legalacsonyabb homerseklet: {met[minindex][0]} {met[minindex][1][0:2:1]}:{met[minindex][1][2:4:1]} {met[minindex][4]}')
print(f'legmagasabb homerseklet: {met[maxindex][0]} {met[maxindex][1][0:2:1]}:{met[maxindex][1][2:4:1]} {met[maxindex][4]}')

#--4--
print('--4--')
szelcsend=[]

for i in range(len(met)):
    if met[i][2]=="000" and met[i][3]=="00":
        szelcsend.append(met[i])

if len(szelcsend)==0:
    print("Nem volt szelcsend a meresek idejen.")
else:
    print('Az alabbi helyeken volt szelcsend:')
    for i in range(len(szelcsend)):
        print(f'{szelcsend[i][0]} {szelcsend[i][1][0:2:1]}:{szelcsend[i][1][2:4:1]}')


#--5--
print('--5--')
tel=[]




for i in range(len(met)):
    if (met[i][0]) not in tel:
        tel.append(met[i][0])
kh=tel.copy()


for i in range(len(met)):
    aktindex=tel.index(str(met[i][0]))
    kh[aktindex]=str(kh[aktindex])+" "+str(met[i][1])+" "+str(met[i][4])

ujkh=[]

for i in range(len(kh)):
    ujkh.append(str(kh[i]).split())

#print(ujkh[0])
print(ujkh[1])

'''
for i in range(len(ujkh)):
    print(i,ujkh[i])
'''