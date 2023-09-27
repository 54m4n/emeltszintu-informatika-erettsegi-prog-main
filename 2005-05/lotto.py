import os


#--- 1, 2 ---
het52=[]
for i in range(5):
    het52.append(int(input(f'kerem az 52. het {i+1}. nyeroszamat: ')))
het52.sort()
print(het52)


het52=[89, 24, 34, 11, 64]

path=(f'{os.path.dirname(__file__)}\src\lottosz.dat')
path2=(f'{os.path.dirname(__file__)}\src\lotto52.ki')
f=open(path,"r")

lottoszamok=[]

for i in range(51):
    lottoszamok.append((f.readline().split()))

f.close()


#--- 3, 4 ---
akthetszam=int(input("kerem a kerdeses het szamat: "))
print(f'a(z) {akthetszam}. het szamai: {lottoszamok[akthetszam-1]}')


#--- 5 ---
mindenszam=[]

for i in range(1,91,1):
    mindenszam.append(i)

k=1

while len(mindenszam)>=0 and k!=90:
    for i in range(51):
        for j in range(5):
            if(int(lottoszamok[i][j]) in mindenszam):
                mindenszam.remove(int(lottoszamok[i][j]))
    k=k+1

if len(mindenszam)==0:
    print("NINCS olyan szam amit ne huztak vna ki")
else:
    print("VAN olyan szam amit nem huztak ki")

#--- 6 ---
paratlan=0
for i in range(len(lottoszamok)):
    for j in range(5):
        if int(lottoszamok[i][j])%2!=0:
            paratlan=paratlan+1

print(f'{paratlan} darab paratlan szam volt')


#--- 7 ---
lottoszamok.append(het52)

f=open(path2,"a")
for i in range(52):
    for j in range(5):
        pass
        f.write(f'{str(lottoszamok[i][j])} ')
    f.write("\n")

f.close()

#--- 8 ---
f=open(path2,"r")
mindenszam = f.read().split()

osszszam=[]

for i in range(90):
    osszszam.append(0)


for i in range(len(mindenszam)):
    aktindex=int(mindenszam[i])-1
    aktertek=osszszam[aktindex]
    aktertek=aktertek+1
    osszszam[aktindex]=aktertek
    #print(osszszam[aktindex],mindenszam[i])
 
print(osszszam)

f.close()



#--- 9 ---

def prime(x):
    fele=round(x/2)
    i=2
    prime=True    
    while x%i!=0 and i<=fele and ((x!=2) or (x!=1)):
        i=i+1
    if i<=fele or x==1:
        prime=False        
    return(prime)

  
   
primek_1_90=[]


for i in range(90):
    if prime(i+1)==True:
        primek_1_90.append(i+1)
        

for i in range(len(primek_1_90)):
    if str(primek_1_90[i]) not in mindenszam:
        print(f'{primek_1_90[i]} primszamot nem huztak ki!')

