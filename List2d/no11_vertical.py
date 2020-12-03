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
def find_vertical(matrix, word):

    position = None
    for i in range(0, len(matrix)):
        word_from_list = ""
        for j in range(0, 3):
            word_from_list += matrix[j][i]
            
        if word_from_list == word:
            position = i

    return position


# testing
string = ["a", "a", "a"]
print(string)

matrix = words_matrix(string)

val = input("kata yang dicari: ")
print("ditemukan di kolom: ", find_vertical(matrix, val))