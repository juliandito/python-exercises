def driver_function(ans_str):
    key_list = list("ACAADBCACBADCADCBBDA")         #convert kunci jawaban ke list
    ans_list = list(ans_str.replace(" ",""))        #hilangin space trus conveert ke list
    wrong_ans_list = []                             #inisialisasi list nomor yang salah
    wrongAns = 0                                    #inisialisasi jumlah jawaban salah

    for i in range(0, len(key_list)):
        if ans_list[i] != key_list[i]:
            wrongAns += 1
            wrong_ans_list.append(i)
    
    return (20-wrongAns), wrongAns, wrong_ans_list

result = driver_function("A A A A B B B B C C C C D D D D E E E E")
print("benar: ", result[0])
print("salah: ", result[1])
print("list salah: ", result[2])
print("To pass thee exam you need to score 15 out of 20")