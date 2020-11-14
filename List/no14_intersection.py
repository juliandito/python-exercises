def sum_list(source1, source2):
    flagSameElement = []

    #cek yang sama
    for i in range(0, len(source1)):
        #cek di list 2
        for j in range(0, len(source2)):
            #kalo ada elemen list 2 yang sama ditandai
            if source1[i] == source2[j]:
                flagSameElement.append(source1[i])
    
    #di casting ke set biar nggak ada duplikasi
    #semoga boleh 
    setSameElement = set(flagSameElement)

    #casting set ke list buat hasil akhir
    target = list(setSameElement)

    #return
    return target


"""
Contoh pemanggilan 
"""
sc1 = [10, 3, 10, 3, 1]
sc2 = [8, 2, 7, 3, 6, 10, 32, 99]

print(sum_list(sc1, sc2))