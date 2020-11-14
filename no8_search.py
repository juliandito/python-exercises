def cari(a, v):
    i = 0
    alamat = -1
    while i < len(a):
        if a[i] == v:
            alamat=i
        i += 1

    return alamat
    
from no4_random import rand
#bikin list pake fungsi nomer 4
value = rand(10, -100, 100)

#pilihan
print("list: ", value)
pilihan = int(input("Dicari: "))
print("Index of {}: {}".format(pilihan, cari(value, pilihan)))