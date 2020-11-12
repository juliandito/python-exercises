def cari(a, v):
    try:
        index = a.index(v)
    except:
        index = -1
    
    return index
    
from no4_random import rand
#bikin list pake fungsi nomer 4
value = rand(10, -100, 100)

#pilihan
print("list: ", value)
pilihan = int(input("Dicari: "))
print("Index of {}: {}".format(pilihan, cari(value, pilihan)))