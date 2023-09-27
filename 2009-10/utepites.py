import os

def atvalt(h,m,s):
    absec=(h*3600)+(m*60)+s
    return absec


# -- 1 --
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}forgalom.txt')
lines=f.readlines()

forgalom=[]
for line in lines:
    forgalom.append(line.strip().split())

del forgalom[0]

# -- 2 --
print("-- 2 --")
#n=int(input("kerem a sorszamot: "))
n=8
print(f'a(z) {forgalom[n-1][3]}. szamu ut innen erkezett: {forgalom[n-1][4]}')

#-- 3 --
print("-- 3 --")
c=0
i=int(len(forgalom)-1)

while c!=2:
    if forgalom[i][4]=="A":
        c=c+1
        if c==1:
            ido2=atvalt(int(forgalom[i][0]),int(forgalom[i][1]),int(forgalom[i][2]))
        if c==2:
            ido1=atvalt(int(forgalom[i][0]),int(forgalom[i][1]),int(forgalom[i][2]))
    i=i-1        
print(f'az utolso 2 jarmu ami F iranyba tartott ennyi mp-kulonbseggel haladt at: {ido2-ido1}')

#-- 4 --

print("-- 4 --")
acount=0
fcount=0
for i in range(len(forgalom)):
    tmpora=forgalom[i][0]
    j=i
    while forgalom[j][0]==tmpora:
        if forgalom[j][4]=="A":
            acount=acount+1
        if forgalom[j][4]=="F":
            fcount=fcount+1
        j=j-1
    try:
        if forgalom[i+1][0]!=tmpora:
            print(f'[{tmpora} ora]\n{acount+fcount} gepjarmu osszesen\n({acount} A iranybol, {fcount} F iranybol)')
    except:
        pass
    acount,fcount=0,0
    i=j

#-- 5 --
print("-- 5 --")
sebessegek=[]
indexek=[]
honnan=[]
for i in range(len(forgalom)):
    seb=round(1000/int(forgalom[i][3]),3)
    if i<=9:    
        sebessegek.append([seb,forgalom[i][4],i])
        
    kicsi=min(sebessegek, key=lambda x:x[0])
    
    if (kicsi[0]<seb) and not any(seb in x for x in sebessegek):
        ind=sebessegek.index(min(sebessegek, key=lambda x:x[0]))
        del sebessegek[ind]
        sebessegek.append([seb,forgalom[i][4],i])
        
    
sebessegek_backup=sebessegek
sebessegek=sorted(sebessegek, key=lambda x:x[0])

print("top 10 sebesseg es indulas")
for i in range(len(sebessegek)):
    print(f'm/s: {sebessegek[i][0]}, honnan: {sebessegek[i][1]}')

#-- 6 --
print("-- 6 --")
belep=0
kilep=0
aelhagy=[]
for i in range(len(forgalom)):
    if forgalom[i][4]=="A":
        belep=belep+int(forgalom[i][0])*3600
        belep=belep+int(forgalom[i][1])*60
        belep=belep+int(forgalom[i][2])
        kilep=belep+int(forgalom[i][3])
        aelhagy.append(kilep)
        belep=0
        kilep=0

def secconvert(seconds):
    h=seconds//3600
    m=(seconds-(h*3600))//60
    s=seconds-(((h*3600))+(m*60))
    return(h,m,s)
    
 
f2=open(f'{path}{os.sep}src{os.sep}\\also.txt','w')

for i in range(len(aelhagy)):
    try:
        if int(aelhagy[i+1])<int(aelhagy[i]):
            aelhagy[i+1]=aelhagy[i]
    except:
        pass
    
    f2.write(f'{secconvert(aelhagy[i])[0]} {secconvert(aelhagy[i])[1]} {secconvert(aelhagy[i])[2]}\n')

f2.close()