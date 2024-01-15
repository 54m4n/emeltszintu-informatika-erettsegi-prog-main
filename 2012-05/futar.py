import os


# -- 1 --

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}tavok.txt')

rows=[]

for line in f:
    rows.append(line.split())

# -- 2 --
print("-- 2 --")
enap=7
unap=0
for i in range(len(rows)):
    if int(rows[i][0])>=unap:
        unap=int(rows[i][0])
    if int(rows[i][0])<=enap:
        enap=int(rows[i][0])
    
i=0
while not(int(rows[i][0])==enap and int(rows[i][1])==1):
    i=i+1

print(f'a het elso utja: {rows[i][2]} km volt')



# -- 3 --
print("-- 3 --")

maxunap=0
for i in range(len(rows)):
    if int(rows[i][0])==unap:
        if int(rows[i][1])>=maxunap:
            maxunap=int(rows[i][1])

for i in range(len(rows)):
    if int(rows[i][0])==unap and int(rows[i][1])==maxunap:
        print(f'a het utso utja: {rows[i][2]} km volt')

# -- 4 --
print("-- 4 --")

hetek=[]

for i in range(7):
    hetek.append(i+1)

for i in range(len(rows)):
    try:
        hetek.remove(int(rows[i][0]))
    except:
        IndexError
    
print(f'a futar az alabbi napokon nem dolgozott: {hetek}')

# -- 5 --
print("-- 5 --")

hetek=[]

for i in range(7):
    hetek.append(i+1)

for i in range(len(rows)):
    hetek[int(rows[i][0])-1]=hetek[int(rows[i][0])-1]+int(rows[i][1])

print(f'a(z) het {hetek.index(max(hetek))+1}. napjan volt a legtobb fuvar')

# -- 6 --
print("-- 6 --")

tavok=[]

for i in range(7):
    tavok.append(0)

for i in range(len(rows)):
    tavok[int(rows[i][0])-1]=tavok[int(rows[i][0])-1]+int(rows[i][2])

print(tavok)

for i in range(len(hetek)):
    print(f'{i+1}. nap: {tavok[i]} km')

# -- 6 --
print("-- 6 --")
'''
1-2 km      - 500 Ft
3-5 km      - 700 Ft
6-10 km     - 900 Ft
11-20 km    - 1 400 Ft
21-30 km    - 2 000 Ft
'''

tav=int(input('kerem a tavot: '))

if tav>=1 and tav<=2:
    osszeg=500
if tav>=3 and tav<=5:
    osszeg=700
if tav>=6 and tav<=10:
    osszeg=900
if tav>=11 and tav<=20:
    osszeg=1400
if tav>=21 and tav<=30:
    osszeg=2000

print(f'{tav} km-re a dijazas: {osszeg} HUF')