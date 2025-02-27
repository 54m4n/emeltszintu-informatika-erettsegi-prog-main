import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}konnyu.txt')

sudoku=[]
stipp=[]
i=0
for l in f:
    if i<=8:
        sudoku.append(l.strip().split())
    else:
        stipp.append(l.strip().split())
    i=i+1
f.close()

#--2--
# ok

#--3--
print('--3--')

row=1
col=1

boxindex=(row-1)//3*3+(col-1)//3+1

if sudoku[row-1][col-1]!=0:
    print(f'az adott helyen ({row} sor, {col} oszlop) szereplo szam: {sudoku[row-1][col-1]}, ({boxindex} mezo)')  

else:
    print(f'a megadott hely nincs meg kitoltve')

#--4--
print('--4--')
c=0
for i in range(9):
    for j in range(9):
        if (int(sudoku[i][j])==0):
            c=c+1

print(c)
print(f'a sudoku feladvany {round(c/(9*9/100),1)}%-a nincs kitoltve meg')

#--5--
print('--5--')
aktsor=[]
aktoszlop=[]
for i in range(len(stipp)):
    aktszam=int(stipp[i][0])
    aktsorsz=int(stipp[i][1])-1
    aktoszlopsz=int(stipp[i][2])-1
    
    aktsor=sudoku[aktsorsz]
    tmp=[]
    for j in range(9):
        tmp.append(sudoku[j][aktoszlopsz])
    aktoszlop.append(tmp)
    
