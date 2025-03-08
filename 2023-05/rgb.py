import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}kep.txt')

pic=[]

for l in f:
    pic.append(l.split())
f.close()


#--2--
print('--2--')

r=180
c=320

print(f'az alabbi koordinata ({r}. sor {c}. oszlop) rgb szine:')
print(pic[r][(c*3)],pic[r][(c*3)+1],pic[r][(c*3)+2])

#--3&4--
print('--3&4--')

count=0
min=int(pic[0][0])+int(pic[0][1])+int(pic[0][2])

for i in range(len(pic)):
    for j in range(0,len(pic[i]),3):
        if (int(pic[i][j])+int(pic[i][j+1])+int(pic[i][j+2])>600):
            count=count+1
        if (int(pic[i][j])+int(pic[i][j+1])+int(pic[i][j+2])<min):
            min=int(pic[i][j])+int(pic[i][j+1])+int(pic[i][j+2])


print(f'vilagos keppontok szama: {count}')  


darkpixels=[]

for i in range(len(pic)):
    for j in range(0,len(pic[i]),3):
        if (int(pic[i][j])+int(pic[i][j+1])+int(pic[i][j+2])==min):
            darkpixels.append([int(pic[i][j]),int(pic[i][j+1]),int(pic[i][j+2])])
print(f'legsotetebb keppont osszege: {min}')
print(f'vilagos keppontok szama: {count}')  

for i in range(len(darkpixels)):
    print(f'RGB({darkpixels[i][0]},{darkpixels[i][1]},{darkpixels[i][2]})')

#--5&6--
print('--5&6--')


def hatar(rownum,dif):  
    bluepixels=[]
    for i in range(2,len(pic[rownum]),3):
        bluepixels.append(int(pic[rownum][i]))
    i=1
    van=False
    while i<len(bluepixels)-1 and van!=True:
        if abs(bluepixels[i]-bluepixels[i+1])>10:
            van=True
        i=i+1    
    return van



k=0

while hatar(k,10)!=True:
    k=k+1

print(f'a felho legfelso sora: {k+1}')

k=len(pic)-1

while hatar(k,10)!=True:
    k=k-1

print(f'a felho legalso sora: {k+1}')