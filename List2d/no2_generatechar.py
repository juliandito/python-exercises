import random   # import di function
def generate_matrix_char(rows, cols):

    result_list = []

    # cara 1
    for i in range(0, rows):
        col_list = []

        for j in range(0, cols):
            rand_char = chr(random.randint(97, 122))    # ascii a = 97, z=122 trus convert ke char
            col_list.append(rand_char)

        result_list.append(col_list)
    
    # cara 2
    # result_list = [[chr(random.randint(97, 122)) for i in range(cols)] for j in range(rows)]
        
    return result_list



# testing
rows = int(input("Jumlah row: "))
cols = int(input("Jumlah col: "))

result = generate_matrix_char(rows, cols)

print(result)