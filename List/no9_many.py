def many(a, v):
    index = []
    for i in range(0, len(a)):
        if a[i] == v:
            index.append(i)
    
    return index

value = [94, 96, -32, -19, -28, 96, -22, 71, 24, -32]

#pilihan
print("list: ", value)
pilihan = int(input("Dicari: "))
print("Index of {}: {}".format(pilihan, many(value, pilihan)))