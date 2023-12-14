import os
import random as rnd
os.system('cls')

def randomGenerator(s, e, a):
    rndList = []
    for i in range(a):
        rndList.append(rnd.randint(s, e))   
    return rndList


def isPerfect(n):
    if n == 1 or n == 0:
        return False
    else:
        divNumbers = [1]
    for i in range(2, n, 1):
        if n % i == 0:
            divNumbers.append(i)
    
    return sum(divNumbers) == n

    

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
perfectNumbers = []
perfectNumFreq = {}
start = makeNumber(startMessage)
end = makeNumber(endMessage)
amount = makeNumber(amountMessage)


randomNumbers = randomGenerator(start, end, amount)
print(randomNumbers)

for i in randomNumbers:
    if isPerfect(i):
        perfectNumbers.append(i)
        
    
for i in perfectNumbers:
    if i in perfectNumFreq.keys():
        perfectNumFreq[i] += 1
    
    else:
        perfectNumFreq[i] = 1

for key in perfectNumFreq.keys():
    print(f'{key}: {perfectNumFreq[key]} db')