def stats(val):
    smallest = min(val)
    largest = max(val)
    total = sum(val)
    average = total / len(val)
    return smallest, largest, total, average



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