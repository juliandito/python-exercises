def add_2d_list(mtx1, mtx2):
    result = []

    for i in range(0, 3):
        result.append([])
        for j in range(0,2):
            result[i].append(mtx1[i][j]+mtx2[i][j])
    
    return result

input_num = input("Input 12 numbers: ").split()
matrix1 = []
matrix2 = []

rows = []
for i in range(0, 6):
    rows.append(int(input_num[i]))
    if len(rows) == 2:
        matrix1.append(rows)
        rows = []

rows = []
for i in range(6, 12):
    rows.append(int(input_num[i]))
    if len(rows) == 2:
        matrix2.append(rows)
        rows = []


print("Hasil: ", add_2d_list(matrix1, matrix2))