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

    return result_list

def stats(matrix):

    smallest = 0
    largest = 0
    total = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            total += matrix[i][j]
            if matrix[i][j] > largest:
                largest = matrix[i][j]
            
            if matrix[i][j] < smallest:
                smallest = matrix[i][j]

    return smallest, largest, total, total/(len(matrix) * len(matrix[i]))
    
# testing
rows = int(input("Jumlah row: "))
cols = int(input("Jumlah col: "))
high = int(input("high: "))
low = int(input("low: "))
val = input("float/int: ")

list_of_num = print_matrix(rows, cols, high, low, val)
result = stats(list_of_num)

print("smallest: ", result[0])
print("largest: ", result[1])
print("total: ", result[2])
print("avg: ", result[3])
