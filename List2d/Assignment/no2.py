def largest_even(mtx):
    largest_even_num = 0
    for i in range(0, len(mtx)):
        for j in range(0, len(mtx[i])):
            if mtx[i][j] % 2 == 0:
                if mtx[i][j] > largest_even_num:
                    largest_even_num = mtx[i][j]
                    large = [mtx[i][j]]
    
    return large

# test
dummy_list = [[1, 8],[3, 4],[5, 6]]
print("List: ", dummy_list)
print("Hasil: ", largest_even(dummy_list))