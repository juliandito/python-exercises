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

    for i in range(0, cols):
        print("\t", i, end="")

    print("")

    for i in range(0, rows):
        print(i, end="")
        for j in range(0, cols):
            print("\t" ,result_list[i][j], end="")
    
        print("")

    return result_list

def find_position(matrix):

    smallest = 0
    largest = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] > largest:
                largest = matrix[i][j]
                largest_position = [i, j]
            
            if matrix[i][j] < smallest:
                smallest = matrix[i][j]
                smallest_position = [i, j]

    return smallest, smallest_position, largest, largest_position
    
# testing
rows = int(input("Jumlah row: "))
cols = int(input("Jumlah col: "))
high = int(input("high: "))
low = int(input("low: "))
val = input("float/int: ")

list_of_num = print_matrix(rows, cols, high, low, val)
result = find_position(list_of_num)

print("smallest: ", result[0])
print("smal pos: ", result[1])
print("largest: ", result[2])
print("large pos: ", result[3])
