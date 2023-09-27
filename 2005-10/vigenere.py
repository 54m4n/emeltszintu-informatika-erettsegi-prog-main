import os

def atalakit(s):
    ujszo=""
    for i in range(len(s)):
        if s[i]!=" ":
            ujszo=ujszo+s[i]
    return ujszo.upper()

def osszefuz(szo):
    m=0
    ujkulcsszoveg=""
    for j in range(len(nyiltszoveg)):
        ujkulcsszoveg=ujkulcsszoveg+kulcsszoveg[m]
        m=m+1
        if m==len(kulcsszoveg):
            m=0
    return ujkulcsszoveg

path=os.path.dirname(__file__)
f=open(f'{path}\src\Vtabla.dat',"r")

kodtabla=[]
kodtabla=f.read().split()

# --- 1, 2, 3 ---
nyiltszoveg=""
while len(nyiltszoveg)==0 or len(nyiltszoveg)>=255:
    nyiltszoveg=input("kerem a 255 karakternel NEM hosszabb szoveget: ")
    #nyiltszoveg="EZAPROBASZOVEGAMITKODOLUNK"
    nyiltszoveg=atalakit(nyiltszoveg)

# --- 4 --- leszarom, hogy kell vagy nemkell ellenorzes vagy atalakitas, gondolom nemfognak seggbekurni ha megcsinalom mert szorgalmas vagyok
kulcsszoveg=""
kulcsszoveg=input("kerem az 5-nel nem hosszabb KULCSszot: ")
#kulcsszoveg="auto"
# --- 5 ---
kulcsszoveg=atalakit(osszefuz(kulcsszoveg))

# --- 6 ---
kodoltszoveg=""

for z in range(len(nyiltszoveg)):
    kar=nyiltszoveg[z]
    megvan=False
    i=0
    while megvan!=True:
        if kodtabla[i][0]==kar:
            megvan=True
        else:
            i=i+1        

    sorszam=i

    kar=kulcsszoveg[z]
    megvan=False
    i=0
    while megvan!=True:
        if kodtabla[0][i]==kar:
            megvan=True
        else:
            i=i+1
    oszlopszam=i

    kodoltszoveg=kodoltszoveg+kodtabla[sorszam][oszlopszam]


print(f'nyilt szoveg: {nyiltszoveg}')
print(f'kulcs szoveg: {kulcsszoveg}')
print(f'kodolt szoveg: {kodoltszoveg}')

# --- 7 ---
f2=open(f'{path}\src\kodolt.dat',"w")
f2.write(kodoltszoveg)


f.close()
f2.close()