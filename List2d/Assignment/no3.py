def flatten_2d(mtx):
    result = []

    for i in range(0, len(mtx)):
        for j in range(0, len(mtx[i])):
            result.append(mtx[i][j])
    
    return result

# test
dummy_list = [["a", "b"],["c", "d"],["e", "f"]]
print("Before: ", dummy_list)
print("Hasil: ", flatten_2d(dummy_list))