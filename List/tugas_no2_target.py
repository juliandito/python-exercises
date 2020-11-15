from tugas_no1_readpositive import read_positive

def target(theList, theTarget):
    targetDitemukan = []
    for i in range(0, len(theList)):
        if theList[i] == theTarget:
            targetDitemukan.append(i)
    
    return targetDitemukan

listForSearch = read_positive()
print("The List: " , listForSearch)
searchedVal = int(input("Masukkan target: "))
print("Posisi target: ", target(listForSearch, searchedVal))