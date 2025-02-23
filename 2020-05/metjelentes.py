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



aktkh=[]
aktmeres=[]

for i in range(len(ujkh)):    
    maxh=int(ujkh[i][2])
    minh=maxh
    for j in range(1,len(ujkh[i])):        
        if len(ujkh[i][j])==4 and (ujkh[i][j][0:2:1]=="01" or ujkh[i][j][0:2:1]=="07" or ujkh[i][j][0:2:1]=="13" or ujkh[i][j][0:2:1]=="19"):
            aktmeres.append(ujkh[i][j][0:2:1])
            aktkh.append(int(ujkh[i][j+1]))
        if j%2==0 and int(ujkh[i][j])>maxh:
            maxh=int(ujkh[i][j])
        if j%2==0 and int(ujkh[i][j])<minh:
            minh=int(ujkh[i][j])

    if "01" in aktmeres and "07" in aktmeres and "13" in aktmeres and "19" in aktmeres:
        valid=True
        sumkh=0
        for l in range(len(aktkh)):
            sumkh=sumkh+aktkh[l]
    else:
        valid=False   
    
    if valid==True:
        print(f'{ujkh[i][0]} kozephomerseklet: {round(sumkh/len(aktkh))}; homerseklet-ingadozas: {maxh-minh}')
    else:
        print(f'{ujkh[i][0]} N/A; homerseklet-ingadozas: {maxh-minh}')

    aktmeres=[]
    aktkh=[]

#nemmondom, ez^ megfingatott, de akarhany sorban is, meglett irva ugyhogy kuss

#--6--
print('--6--')
kh=tel.copy()
aktindex=0
for i in range(len(met)):
    aktindex=tel.index(str(met[i][0]))
    kh[aktindex]=str(kh[aktindex])+" "+str(met[i][1])+" "+str(int(met[i][3]))

ujkh=[]
for i in range(len(kh)):
    ujkh.append(str(kh[i]).split())


f2=open(f'{path}{os.sep}src{os.sep}test.txt','w')


beir=""
for i in range(0,len(ujkh)):
    if i!=0:
        beir=beir+str(f'\n{ujkh[i][0]}')
    else:
        beir=beir+str(f'{ujkh[i][0]}')
    for j in range(1,len(ujkh[i]),2):   
        beir=beir+str(f'\n{ujkh[i][j]} ')
        for k in range(int(ujkh[i][j+1])):
            beir=beir+str('#')
f2.write(beir)
f2.close()

#btw nemfogok telepulesenkent kulon file-t letrehozni mert a githubra feltoltott szemetnek is van hatara... maradjunk annyiban, hogy ez innentol gyerekjatek