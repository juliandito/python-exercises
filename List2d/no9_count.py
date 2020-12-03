import random   # import di function

# method buat bikin matrix
def print_matrix_char(rows, cols):

    result_list = []

    for i in range(0, rows):
        col_list = []

        for j in range(0, cols):
            rand_char = chr(random.randint(97, 122))    # ascii a = 97, z=122 trus convert ke char
            col_list.append(rand_char)

        result_list.append(col_list)
        
    for i in range(0, cols):
        print("\t", i, end="")

    print("")

    for i in range(0, rows):
        print(i, end="")
        for j in range(0, cols):
            print("\t" ,result_list[i][j], end="")
    
        print("")
    
    return result_list


# method buat cari freq
def count_freq(matrix, val):
    count = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == val:   
                count += 1

    return count


# testing
rows = int(input("Jumlah row: "))
cols = int(input("Jumlah col: "))

matrix = print_matrix_char(rows, cols)
val = input("masukkan char: ")
print("count of ", val," : ", count_freq(matrix, val))