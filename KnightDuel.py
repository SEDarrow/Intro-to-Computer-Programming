# whatever_you_name_your_driver.py
# Sarah Darrow
# sd1209
# 11/9/15
#
# This program fights two knights

from knight import *
from time import sleep


def getKnightInfo(number, name = '', low = ''):
    if name == '':
        name = input("What would you like to name your "+number+" knight? ")
    if low == '':
        low = input("What is the minimum amount of damage that "+name+" will do on an attack? ")
        try:
            low = int(low)
        except ValueError:
            print("Enter a number!")
            return getKnightInfo(number, name)
        
    high = input("What is the maximum amount of damage that "+name+" will do on an attack? ")
    try:
        high = int(high)
        if high < low:
            raise IndexError
    except ValueError:
        print("Enter a number!")
        return getKnightInfo(number, name, low)  
    except IndexError:
        print("Max damage must be more than min damage")
        return getKnightInfo(number, name, low)   
    
    return name, high, low

info = getKnightInfo("first")
k1 = Knight(info[0], info[1], info[2])
print('')

info = getKnightInfo("second")
k2 = Knight(info[0], info[1], info[2])

i = 0
knights = [k1, k2]

print("")
print(k1, k2, "\n")

while k1.hasLimbs() and k2.hasLimbs():
    knights[i%2].attack(knights[(i+1)%2])
    print(k1, k2)
    sleep(1)
    i+=1
    print("")
    
print(knights[(i-1)%2].name, "is the winner! (But we'll call it a draw)")
