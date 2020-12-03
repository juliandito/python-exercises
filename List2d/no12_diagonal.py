import random   # import di function

#bikin matrix
def words_matrix(string):

    result_list = []

    for i in range(0, len(string)):
        col_list = []
        list_string = list(string[i])

        for j in range(0, len(list_string)):
            col_list.append(list_string[j])

        result_list.append(col_list)
        
    for i in range(0, len(list_string)):
        print("\t", i, end="")

    print("")

    for i in range(0, len(string)):
        print(i, end="")
        for j in range(0, len(list_string)):
            print("\t" ,result_list[i][j], end="")
    
        print("")
    
    return result_list

# method buat nemu
def find_diagonal(matrix, word):

    position = "Not found"

    # 0.0 ke n.n
    for i in range(0, len(matrix)):
        word_from_list = ""
        for j in range(0, len(matrix[i])):
            word_from_list += matrix[j][j]

        if word_from_list == word:
            position = "Found"
    
    # # n.0 ke n.0
    # for i in range(len(matrix)-1, 0, -1):
    #     word_from_list = ""
    #     for j in range(0, len(matrix[i])):
    #         word_from_list += matrix[j][j]

    #     if word_from_list == word:
    #         position = "Found"

    return position


# testing
string = ["cat", "dog", "big"]
print(string)

matrix = words_matrix(string)

val = input("kata yang dicari: ")
print("Status: ", find_diagonal(matrix, val))