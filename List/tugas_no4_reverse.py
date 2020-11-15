from tugas_no1_readpositive import read_positive

def reverse_list(theList):
    revList = []
    panjang = len(theList) -1
    for i in range(panjang, -1, -1):
        revList.append(theList[i])
    
    print("Rev List: ",revList)

listForSearch = read_positive()
print("The List: ", listForSearch)
reverse_list(listForSearch)