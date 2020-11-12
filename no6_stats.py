def stats(val):

    smallest = val[0]
    largest = 0
    total = 0

    for i in range(0, len(val)):
        total += val[i]
        if val[i] > largest:
            largest = val[i]
        elif val[i] < smallest:
            smallest = val[i]

    return smallest, largest, total, total/len(val)


from no4_random import rand
#bikin list pake fungsi nomer 4
value = rand(10, -100, 100)

#panggil fungsi stats
#hasil dalam bentuk list
result = stats(value)
print("list: ", value)
print("smol: " , result[0])
print("large: " , result[1])
print("total: " , result[2])
print("avg: " , result[3])