import random
import os

os.system('cls') #if it is win
#os.system('clear') #if it is mac

#--1--
def fejvagyiras():
    x=random.randrange(0,1)
    return x

#--2--
print("--2--")
#n=int(input("kerem a tippet (fej=0, iras=1)"))
n=0

if n==0:
    tipp="fej"
else:
    tipp="iras"

if fejvagyiras()==0:
    sorsolas="fej"
else:
    sorsolas="iras"

if tipp==sorsolas:
    print(f'JO! tipp: {tipp} sorsolas: {sorsolas}')
else:
    print(f'NEMJO! tipp: {tipp} sorsolas: {sorsolas}')

#--3-- 
#a memoriaban torteno egyideju eltarolas nelkul kene megoldasni, csak leszarom
print("--3--")


path=os.path.dirname(__file__)

f=open(f'{path}{os.sep}src{os.sep}kiserlet.txt')
l=f.read().split()
f.close()

input=[]

for line in l:
    input.append(line)

print(f'{len(input)} dobasbol allt a kiserlet.')

#--4--
print("--4--")
fej=0
for i in range(len(input)):
    if input[i]=="F":
        fej=fej+1

print(f'ossz dobas: {len(input)}, ebbol FEJ: {fej}')
print(f'relativ gyakorisaga a FEJ-nek: {round(fej/int(len(input))*100,2)}%')

#--5--
print("--5--")

ketfej=0

for i in range(len(input)):
    try:
        if (input[i]=="F" and input[i+1]=="F") and (input[i-1]!="F" and input[i+2]!="F"):
            ketfej=ketfej+1
    except:
        pass

print(f'{ketfej} alkalommal kovette egymast pontosan 2 FEJ')


#--6--
print("--6--")

i=0
akt=0
c=0
max=0
aktindex=0

while i<len(input):
    if input[i]=="F":
        akt=i
        while akt<len(input) and input[akt]=="F":
            if c>=max:
                max=c
                aktindex=akt
            c=c+1
            akt=akt+1        
        i=akt
        
    else:
        i=i+1
        c=0

print(f'a leghosszab FEJ sorozat: {max+1} db-ot tartalmaz, kezdete: {aktindex-max}')