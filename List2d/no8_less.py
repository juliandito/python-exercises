import random   # import di function
def print_int_matrix(rows, cols, high, low):

    result_list = []

    # cara 1
    for i in range(0, rows):
        col_list = []

        for j in range(0, cols):
            rand_num = random.randint(low, high)
            col_list.append(rand_num)

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

def find_less(matrix, num):

    list_pos = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] < num:
                list_pos.append([i, j])

    return list_pos[0]
    
# testing
rows = int(input("Jumlah row: "))
cols = int(input("Jumlah col: "))
high = int(input("high: "))
low = int(input("low: "))
search_num = int(input("yang dicari: "))

list_of_num = print_int_matrix(rows, cols, high, low)
result = find_less(list_of_num, search_num)

print("position: ", result)     #hasil
print("value: ", list_of_num[result[0]][result[1]])  