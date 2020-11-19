def val_code(str):
    pc_status ="not valid"
    pi_status ="not valid"
    pq_status ="not valid"

    pc = str[0:3]
    pi = str[3:7]
    pq = str[7:len(str)]

    if pc.isupper():
        pc_status = "valid"
    
    if pi.isdigit():
        pi_status = "valid"
    
    if pq[0].isupper():
        pq_status = "valid"

    
    print("Cat ", pc, " is ", pc_status)
    print("ID ", pi, " is ", pi_status)
    print("Qualifier ", pq, " is ", pq_status)

val_code("aTV34b2s1124")