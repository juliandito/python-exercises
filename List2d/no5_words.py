import random   # import di function
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



# testing
string = ["catt", "dogg", "bigg"]

words_matrix(string)
