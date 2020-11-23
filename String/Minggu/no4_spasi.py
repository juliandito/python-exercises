def add_space(str_input):
    list_str = list(str_input)  
    list_upper = []             #bikin list kapital

    list_string_hasil = []      #declare string hasil
    lenght = 0                  #buat nandain huruf terakhir

    #isi list yang kapital
    for i in range(0, len(list_str)):
        if list_str[i].isupper():
            list_upper.append(i)
        elif i == (len(list_str)-1):
            list_upper.append(i)
            lenght = i

    #huruf pertama
    list_string_hasil.append(list_str[0])
    #kata pertama
    for j in range(list_upper[0]+1, list_upper[1]):
        list_string_hasil.append(list_str[j].casefold())

    list_string_hasil.append(" ")

    #kata lain
    for i in range(1, len(list_upper)-1):
        for j in range(list_upper[i], list_upper[i+1]):
            list_string_hasil.append(list_str[j].casefold())

        list_string_hasil.append(" ")

    #dijadiin string
    glue = ""
    string_hasil = glue.join(list_string_hasil).strip()

    #tambah huruf terakhir
    string_hasil += str_input[lenght]
    return string_hasil


stringPercobaan = "TesDuaKata"
print(add_space(stringPercobaan))