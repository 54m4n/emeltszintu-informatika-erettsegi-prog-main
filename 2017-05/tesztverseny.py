import os
import sys

os.system('cls') #if it is win
#os.system('clear') # if it is unix

#--1--

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}valaszok.txt')
l=f.read().split('\n')
f.close()

goodanswers=l[0]
answers=[]

for i in range(1,len(l)):
    answers.append(l[i].split())

#--2--
print('--2--')
print(f'A versenyen {len(answers)} versenyzo vett reszt.')

#--3--
print('--3--')

competitornum="CX616"

for i in range(len(answers)):
    if answers[i][0]==competitornum:
        choosencompetitoranswer=answers[i][1]
        print(f'A versenyzo azonositoja: {competitornum}, valasza: {answers[i][1]}')
        break
#--4--
print('--4--')
print(f'helyes megoldas: {goodanswers}')
print(f'valasztott versenyzo megoldas: {choosencompetitoranswer}')

out=""

for i in range(len(choosencompetitoranswer)):
    if choosencompetitoranswer[i]==goodanswers[i]:
        out=out+"+"
    else:
        out=out+" "
print(f'a versenyzo helyes valaszai: {out}')

#--5--
print('--5--')
tasknum=9
c=0

for i in range(len(answers)):
    if (answers[i][1][tasknum]==goodanswers[tasknum]):
        c=c+1
    
print(f'feladat sorszama: {tasknum+1}, a feladatra {c} fo, a versenyzok {round(c/(len(answers)/100),2)}%-a valaszolt helyesen.')

#--6--
print('--6--')

scores=[]

for i in range(len(answers)):
    s=0
    for j in range(len(answers[i][1])):
        if answers[i][1][j]==goodanswers[j]:
            if j+1>=1 and j+1<=5:
                s=s+3
            if j+1>=6 and j+1<=10:
                s=s+4
            if j+1>=11 and j+1<=13:
                s=s+5
            if j+1==14:
                s=s+6
    scores.append([answers[i][0],s])
    s=0

f=open(f'{path}{os.sep}src{os.sep}pontok.txt','w')
for i in range(len(scores)):
    f.write(f'{scores[i][0]} {scores[i][1]}\n')
f.close()

#--7--
print('--7--')

scores.sort(key=lambda x: x[1])
scores.reverse()

top3=[scores[0][1],scores[1][1],scores[2][1]]

prices=[]

for i in range(len(scores)):
    if scores[i][1]>=top3[0]:
        prices.append(scores[i])
        top3[0]=scores[i][1]
    if scores[i][1]<top3[0] and scores[i][1]>=top3[1]:
        prices.append(scores[i])
        top3[1]=scores[i][1]
    if scores[i][1]<top3[1] and scores[i][1]>=top3[2]:
        prices.append(scores[i])
        top3[2]=scores[i][1]

for i in range(len(prices)):
    print(prices[i])