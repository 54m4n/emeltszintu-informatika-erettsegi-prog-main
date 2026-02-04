import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--
print('--1--')

print(os.path.dirname(__file__))