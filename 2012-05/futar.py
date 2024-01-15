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









print(f'utso ut km: {rows[len(rows)-1][2]} km')


