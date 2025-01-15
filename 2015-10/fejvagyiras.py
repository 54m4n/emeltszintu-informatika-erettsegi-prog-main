import random
import os


#--1--
def fejvagyiras():
    x=random.randrange(0,1)
    return x

#--2--
#n=int(input("kerem a tippet (fej=0, iras=1)"))
n=0

if n==0:
    tipp="fej"
else:
    tipp="iras"

if fejvagyiras()==0:
    sorsolas="fej"
else:
    sorsolas="iras"

if tipp==sorsolas:
    print(f'JO! tipp: {tipp} sorsolas: {sorsolas}')
else:
    print(f'NEMJO! tipp: {tipp} sorsolas: {sorsolas}')

