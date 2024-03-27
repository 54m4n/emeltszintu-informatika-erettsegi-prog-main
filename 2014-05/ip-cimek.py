import os

#--1--

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}ip.txt','r')

ip=[]
ipk=[]
for i in f:
    ip.append(i.split())
    ipk.append(i)

f.close()
#--2--
print('--2--')
print(f'{len(ip)}. sor van az allomanyban')

#--3--
print('--3--')
print(sorted(ipk)[0])

#--4--
print('--4--')

dok=0 #2001:0db8
glo=0 #2001:0e
egy=0 #fc vagy fd


for i in range(len(ip)):
    if (str(ip[i])[2:11:1])=='2001:0db8':
        dok=dok+1
    if (str(ip[i])[2:9:1])=='2001:0e':
        glo=glo+1        
    if (str(ip[i])[2:4:1])=='fc' or (str(ip[i])[2:4:1])=='fd':
        egy=egy+1

print(f'dokumentacios ip cim: {dok}\nglobalis egyedi ip cim: {glo}\nhelyi egyedi ip cim: {egy}')
        
#--5--
f2=open(f'{path}{os.sep}src{os.sep}sok.txt','w')

for i in range(len(ip)):
    if (str(ip[i]).count('0'))>=18:
        f2.write(f'{i+1}. {str(ip[i])[2:len(str(ip[i]))-2:1]}\n')
f2.close()


#--6--
print('--6--')

#szam=int(input('kerek egy sorszamot: '))

szam=10

rov=str(ip[szam-1]).replace("'",'').replace('[','').replace(']','').split(':')

print(str(rov).replace("'",'').replace(',','').replace('[','').replace(']','').replace(" ",":"))




for i in range(len(rov)):
    j=0
    if rov[i][j]=='0':
        while j<=2 and rov[i][j]=='0':
            j=j+1
        rov[i]=rov[i][j:len(rov[i]):1]
    
aktipaddr=str(rov).replace("'",'').replace(',','').replace('[','').replace(']','').replace(" ",":")

print(aktipaddr)

if aktipaddr.find(":0:")!=-1:
    while aktipaddr.find(":0:")>-1:
        aktipaddr=aktipaddr.replace(':0:','::')
    while aktipaddr.find(':::')>-1:
        aktipaddr=aktipaddr.replace(':::','::')
    
    print(aktipaddr)

else:
    print(f'{aktipaddr} tovabb mar nem roviditheto')


