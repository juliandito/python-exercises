import random

def rand(n, low, high):
    #deklarasi
    myList = []

    #looop
    for i in range(0, n):
        angkaRandom = random.randint(low, high)
        myList.append(angkaRandom)
    
    #return
    myList.sort()
    return myList
