def sum_list(source1, source2):
    target = []
    for i in range(0, len(source1)):
        sumResult = source1[i] + source2[i]
        target.append(sumResult)
    
    return target

sc1 = [10, 3, 10, 3, 1]
sc2 = [8, 2, 7, 3, 6]

print(sum_list(sc1, sc2))