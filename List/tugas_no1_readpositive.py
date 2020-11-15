def read_positive():
    #inisialisasi list sama kontrol loopignnya
    inputLoop = True
    initList = []

    while inputLoop:
        inputUser = int(input("Enteer a positive number: "))
        #cek input negatif, kalo ya maka terus loop sampe positif
        while inputUser < 0:
            inputUser = int(input("Enteer a positive number: "))

        #cek apakah 0, kalo ga 0 bakal di insert
        if inputUser == 0:
            inputLoop = False
        else:
            initList.append(inputUser)
    
    #reeturn listnya tadi
    return initList

"""
cara manggilnya,  
"""