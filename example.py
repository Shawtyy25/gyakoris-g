import os
import random as rnd
os.system('cls')

def randomGenerator(s, e, a):
    rndList = []
    for i in range(a):
        rndList.append(rnd.randint(s, e))   
    return rndList


        

def isPerfect():
    pass

def makeNumber(text):
    
    while True:
        num = input(text)

        try: 
            num = int(num)
            return num

        except ValueError:
            print('helytelen érték')


startMessage = 'Kezdő érték: '
endMessage = 'Végérték: '
amountMessage = 'Értékek száma: '

start = makeNumber(startMessage)
end = makeNumber(endMessage)
amount = makeNumber(amountMessage)

