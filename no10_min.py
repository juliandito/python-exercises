def many(a):
    index = []
    dicari = min(a)
    for i in range(0, len(a)):
        if a[i] == dicari:
            index.append(i)
    
    return index


value = [94, 96, -32, -19, -28, 96, -22, 71, 24, -32]
print("list: ", value)
print("Index of minimum: {}".format(many(value)))