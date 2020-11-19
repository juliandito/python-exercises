def parse_code(str):
    pc = str[0:3]
    pi = str[3:7]
    pq = str[7:len(str)]

    return pc, pi, pq

result = parse_code("ATV3482S14")

print("Cat: ",result[0])
print("ID: ",result[1])
print("Qualifiers: ",result[2])