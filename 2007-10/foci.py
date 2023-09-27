import os

# -- 1 --
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}meccs.txt','r')
meccsek=[]
for i in range(int(f.readline())):
    meccsek.append(f.readline().split())

# -- 2 --
print("-- 2 --")
fordulo=int(input("kerem a fordulo szamat: "))
#fordulo=8
for i in range(len(meccsek)):
    if int(meccsek[i][0])==fordulo:
        print(f'{meccsek[i][5]}-{meccsek[i][6]}: {meccsek[i][1]}-{meccsek[i][2]} ({meccsek[i][3]}-{meccsek[i][4]})')

# -- 3 --
print("-- 3 --")
for i in range(len(meccsek)):
    if meccsek[i][3]<meccsek[i][4] and meccsek[i][1]>meccsek[i][2]:
        print(f'{i} - a(z) {meccsek[i][0]}. forduloban a(z) {meccsek[i][5]} csapat forditott!')
    if meccsek[i][4]<meccsek[i][3] and meccsek[i][1]<meccsek[i][2]:
        print(f'{i} - a(z) {meccsek[i][0]}. forduloban a(z) {meccsek[i][6]} csapat forditott!')

# -- 4 --
print("-- 4 --")
team=input("kerem a csapat nevet: ")
#team="Bogarak"

# -- 5 --
print("-- 5 --")
lott,kapott=0,0
for i in range(len(meccsek)):
    if meccsek[i][5]==team:
        lott=lott+int(meccsek[i][1])
        kapott=kapott+int(meccsek[i][2])
    if meccsek[i][6]==team:
        lott=lott+int(meccsek[i][2])
        kapott=kapott+int(meccsek[i][1])

print(f'a(z) {team} statja:\nlott: {lott}, kapott: {kapott}')

# -- 6 -- az egy kurvanagy hazugsag amiben a feladat probal segiteni (ehelyett jol szetbassza az idegrendszered. A Bogarak csapata ugyanugy lelett szopatva, nem veretlenek.
print("-- 6 --")
kikapott=False
i=0
while kikapott!=True and i<len(meccsek):
    if meccsek[i][5]==team and int(meccsek[i][1])<int(meccsek[i][2]):
        print(f'a(z) {team} csapat eloszor a(z) {meccsek[i][0]} forduloban lett megbaszva, meghozza a(z) {meccsek[i][6]} altal.')
        kikapott=True
    elif meccsek[i][6]==team and int(meccsek[i][2])<int(meccsek[i][1]):
        print(f'a(z) {team} csapat eloszor a(z) {meccsek[i][0]} forduloban lett megbaszva, meghozza a(z) {meccsek[i][5]} altal.')                
        kikapott=True
        
    else:
        i=i+1

if kikapott==False:
    print(f'a(z) {team} csapat sose lett meg leszopatva...')

# -- 7 --
print("-- 7 --")
vegeredmenyek=[]
for i in range(len(meccsek)):
    if int(meccsek[i][1])>=int(meccsek[i][2]):
        veredmeny=str(f'{meccsek[i][1]}-{meccsek[i][2]}')
    else:
        veredmeny=str(f'{meccsek[i][2]}-{meccsek[i][1]}')
    vegeredmenyek.append(veredmeny)

uniqveredmenyek=[]
    
for i in range(len(vegeredmenyek)):
    if vegeredmenyek[i] not in uniqveredmenyek:
        uniqveredmenyek.append(vegeredmenyek[i])
    
for i in range(len(uniqveredmenyek)):
    print(f'{uniqveredmenyek[i]}: {vegeredmenyek.count(uniqveredmenyek[i])} db.')


