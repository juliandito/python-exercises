import random   # import di function
def print_matrix(rows, cols, high, low, value_type):

    result_list = []

    # cara 1
    for i in range(0, rows):
        col_list = []

        for j in range(0, cols):
            if value_type == "float":
                rand_num = random.uniform(float(low), float(high))
            elif value_type == "int":
                rand_num = random.randint(low, high)
            col_list.append(rand_num)

        result_list.append(col_list)
    
    # cara 2
    # if value_type == "float":
    #     result_list = [[random.uniform(float(low), float(high)) for i in range(cols)] for j in range(rows)]
    # elif value_type == "int":
    #     result_list = [[random.randint(low, high) for i in range(cols)] for j in range(rows)]

    for i in range(0, cols):
        print("\t", i, end="")

    print("")

    for i in range(0, rows):
        print(i, end="")
        for j in range(0, cols):
            print("\t" ,result_list[i][j], end="")
    
        print("")
    
# testing
rows = int(input("Jumlah row: "))
cols = int(input("Jumlah col: "))
high = int(input("high: "))
low = int(input("low: "))
val = input("float/int: ")

print_matrix(rows, cols, high, low, val)
