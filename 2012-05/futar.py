import os

# -- 1 --
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}tavok.txt')
rows=[]
for line in f:
    rows.append(line.split())  
f.close()

# -- 2 --
print(" -- 2 -- ")
elsonap=int(rows[0][0])

i=0
km=0

while elsonap==int(rows[i][0]):
    km=km+int(rows[i][2])
    i=i+1    

print(f'a het legelso utja: {km} km volt')

# -- 3 --
print(" -- 3 -- ")

utsonap=int(rows[len(rows)-1][0])
i=len(rows)-1

km=0

while utsonap==int(rows[i][0]):
    km=km+int(rows[i][2])
    i=i-1    

print(f'a het utolso utja: {km} km volt')

# -- 4 --
print(" -- 4 -- ")

for i in range(len(rows)):
    
    try:
        kulonbseg=(int(rows[i+1][0])-int(rows[i][0])) 
    except:
        IndexError
    print(kulonbseg)
