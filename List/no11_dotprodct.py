def dot(source1, source2):
    target = 0
    for i in range(0, len(source1)):
        target += (source1[i]*source2[i])
    
    return target

sc1 = [10, 3, 10, 3, 1]
sc2 = [8, 2, 7, 3, 6]

print(dot(sc1, sc2))