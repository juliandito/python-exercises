def sum_list(source1, source2):
    flagDuplicateAtSource1 = []
    flagDuplicateAtSource2 = []
    
    #cari elemen sama di list 1
    for i in range(0, (len(source1)-1)):
        for j in range(i+1, len(source1)):
            if source1[j] == source1[i]:
                flagDuplicateAtSource1.append(source1[j])
    #hilangkan elemen sama di list 1
    for i in range(0, len(flagDuplicateAtSource1)):
        source1.remove(flagDuplicateAtSource1[i])

    #cari elemen sama di list 2
    for i in range(0, (len(source2)-1)):
        for j in range(i+1, len(source2)):
            if source2[j] == source2[i]:
                flagDuplicateAtSource2.append(j)

    #tambah elemen yang dari list 1
    flagDuplicateAtSource2.extend(source1)
    #hilangkan elemen sama di list 2
    for i in range(0, len(flagDuplicateAtSource2)):
        try:
            source2.remove(flagDuplicateAtSource2[i])
        except:
            pass

    #gabung list
    source1.extend(source2)
    target = source1
    #return
    return target

sc1 = [10, 3, 10, 3, 1]
sc2 = [8, 2, 7, 3, 6, 10, 32, 99]

print(sum_list(sc1, sc2))