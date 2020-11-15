from tugas_no1_readpositive import read_positive

def largest_odd(theList):
    maxOdd = None
    for i in range(0, len(theList)):
        if theList[i] % 2 != 0:
            maxOdd = theList[i]
        
    if maxOdd == None:
        maxOdd = -1     
    
    return maxOdd

listForSearch = read_positive()
print("The List: " , listForSearch)
print("Biggest Odd: ", largest_odd(listForSearch))