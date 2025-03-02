import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')
'''
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

#--5--
print('--5--')
'''
'''
def hatar(rownum,dif):  
    bluepixels=[]
    for i in range(2,len(pic[rownum]),3):
        bluepixels.append(int(pic[rownum][i]))
    print(bluepixels)
    i=1
    van=False
    while (abs(bluepixels[i]-bluepixels[i-1])<dif or i<len(bluepixels)):
        van=True
        i=i+1
    
    return van

hatar(0,1)
'''



bp=[112,113,113,113,113,113,113,113,115,115,116,116,116,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117]



i=1
print(len(bp))
#while abs(bp[i]-bp[i-1])<=10 or i>len(bp):
while i<=len(bp)-2:
    print(bp[i-1],bp[i],abs(bp[i]-bp[i-1]),i)
    i=i+1

print(bp[i])






'''
k=0
igen=False
while igen!=True:
    if hatar(k,10)==True:
        igen=True
    k=k+1

print(k)
'''
