import os
import platform
import math

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}jel.txt')

tmp=[]
jelek=[]
for l in f:
    tmp.append(int(l.strip().split()[0]))
    tmp.append(int(l.strip().split()[1]))
    tmp.append(int(l.strip().split()[2]))
    tmp.append(int(l.strip().split()[3]))
    tmp.append(int(l.strip().split()[4]))
    
    jelek.append(tmp)
    tmp=[]
f.close()

#--2--
beker=3
print(f'{beker}. meres koordinatai: x->{jelek[beker-1][3]} y->{jelek[beker-1][4]}')

#--3 & 4--
print('--3 & 4--')
def eltelt(h1,m1,s1,h2,m2,s2):
    sec1=(h1*60*60)+(m1*60)+s1
    sec2=(h2*60*60)+(m2*60)+s2
    return sec2-sec1

def totime(sec):
    h=int(sec//(60*60))
    sec=int(sec-(h*(60*60)))
    m=int(sec/60)
    sec=int(sec-(m*60))
    return (f'{h}:{m}:{sec}')

print(f'az elso es utolso meres kozti eltelt ido:')
print(totime(eltelt(jelek[0][0],jelek[0][1],jelek[0][2],jelek[len(jelek)-1][0],jelek[len(jelek)-1][1],jelek[len(jelek)-1][2])))

#--5--
print('--5--')

maxx=jelek[0][3]
maxy=jelek[0][4]
minx=jelek[0][3]
miny=jelek[0][4]

for i in range(len(jelek)):
    if jelek[i][3]>maxx:
        maxx=jelek[i][3]
    if jelek[i][4]>maxy:
        maxy=jelek[i][4]
    if jelek[i][3]<minx:
        minx=jelek[i][3]
    if jelek[i][4]<miny:
        miny=jelek[i][4]
print(f'bal also: {minx} {miny}, jobb felso: {maxx} {maxy}')
    
#--6--
print('--6--')

print(math.sqrt(4))
elma=0
elmb=0
elmc=0
sumelm=0
for i in range(len(jelek)-1):
    elma=abs(jelek[i][3]-jelek[i+1][3])
    elmb=abs(jelek[i][4]-jelek[i+1][4])
    elmc=math.pow(elma,2)+math.pow(elmb,2)
    sumelm=sumelm+math.sqrt(elmc)

print(f'elmozdulas: {round(sumelm,3)} egyseg')

#majd en itt jol nem azzal a keplettel baszakodok ami megvan adva, hanem kibaszottul tudom fejbol hogy itt egy derekszogu haromszog atfogojat kell kiszamolni, szoval majd en tudom, hogy hogycsinalom meg, nemkell segitseg :)

#--7--
print('--7--')
idodelta=0
koordelta=0
delta=0
idelta=0
kdelta=0
for i in range(1,len(jelek)):
    delta=0
    idelta=0
    kdelta=0
    idodelta=eltelt(jelek[i-1][0],jelek[i-1][1],jelek[i-1][2],jelek[i][0],jelek[i][1],jelek[i][2])
    if idodelta>300:
        idelta=int((idodelta-300)//300)
    if abs(jelek[i-1][3]-jelek[i][3])>10 or abs(jelek[i-1][4]-jelek[i][4])>10:
        kdelta1=int(abs(jelek[i-1][3]-jelek[i][3])//10)
        kdelta2=int(abs(jelek[i-1][4]-jelek[i][4])//10)
        if kdelta1>kdelta2:
            kdelta=kdelta1
        else:
            kdelta=kdelta2
    if idelta>kdelta:
        print(f'{jelek[i][0]} {jelek[i][1]} {jelek[i][2]} - idoelteres {idelta}')
    if idelta<kdelta:
        print(f'{jelek[i][0]} {jelek[i][1]} {jelek[i][2]} - koordinata-elteres {kdelta}')


#ezt is lehoztam kurvagyorsan, ez kiraly volt!!