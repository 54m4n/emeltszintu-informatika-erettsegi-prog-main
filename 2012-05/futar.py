import os


# -- 1 --

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}tavok.txt')

rows=[]

for line in f:
    rows.append(line.split())

# -- 2 --
print("-- 2 --")
print(f'elso ut km: {rows[0][2]} km')

# -- 3 --
print("-- 3 --")

i=0
km=0

for i in range(len(rows)):
    km=int(rows[i][2])
    if(int(rows[i][0])>int(rows[i+1][0])):
        break

print(f'a het utso napja: {km} km')




# -- 4 --
print(" -- 4 -- ")


hetnapok=[]
hetszama=1
for i in range(7):
    hetnapok.append(i+1)

tmp_hetnapok=hetnapok.copy()

for i in range(len(rows)):
    
    try:
        hetnapok.remove(int(rows[i][0]))
    except:
        IndexError
    
    try:
        if int(rows[i][0])>int(rows[i+1][0]):
            print(f'a(z) {hetszama}. heten a futar az alabbi napokon nem dolgozott: {hetnapok}')
            hetnapok=tmp_hetnapok.copy()
            hetszama=hetszama+1
            
    except:
        IndexError
        if IndexError:

            hetnapok=tmp_hetnapok.copy()
            hetnapok.remove(int(rows[i][0]))
            print(f'a(z) {hetszama}. heten a futar az alabbi napokon nem dolgozott: {hetnapok}')
            
            
