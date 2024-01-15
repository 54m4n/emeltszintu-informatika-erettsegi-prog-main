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

