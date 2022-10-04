def cari_diff(source1, source2):
    
    #pake build-in function
    target = list(set(source1).symmetric_difference(source2))
    #return
    return target

"""
Contoh pemanggilan 

"""
sc1 = [10, 3, 10, 3, 1]
sc2 = [8, 2, 7, 3, 6, 10, 32, 99]

print(cari_diff(sc1, sc2))