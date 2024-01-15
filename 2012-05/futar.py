import os


# -- 1 --

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}tavok.txt')

rows=[]

for line in f:
    rows.append(line.split())


print(rows[0])

# -- 2 --
print("-- 2 --")

elsonap=rows[0][0]

i=0
allkm=0
while rows[i][0]==elsonap:
    allkm=int(allkm)+int(rows[i][2])
    i=i+1

print(allkm)