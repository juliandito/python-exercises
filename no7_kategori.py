def kategori(val):

    flagNegative = 0
    flagPositive = 0
    flagZeroes = 0
    flagEven = 0
    flagOdd = 0


    for i in range(0, len(val)):
        if val[i] > 0:
            flagPositive += 1
            if val[i] % 2 == 0:
                flagEven += 1
            else:
                flagOdd += 1

        elif val[i] < 0:
            flagNegative += 1
            if val[i] % 2 == 0:
                flagEven += 1
            else:
                flagOdd += 1

        else:
            flagZeroes += 1
    
    return flagNegative, flagPositive, flagZeroes, flagEven, flagOdd

from no4_random import rand
#bikin list pake fungsi nomer 4
value = rand(10, -100, 100)

#panggil fungsi kategori
#hasil dalam bentuk list
result = kategori(value)
print("list: ", value)
print("neg: " , result[0])
print("pos: " , result[1])
print("zero: " , result[2])
print("even: " , result[3])
print("odd: " , result[4])