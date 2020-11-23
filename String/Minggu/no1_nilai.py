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


inputUser = input("Masukkan list jawaban, uppercase : ")
result = driver_function(inputUser)
print("benar: ", result[0])
print("salah: ", result[1])
print("list salah: ", result[2])
print("To pass thee exam you need to score 15 out of 20")