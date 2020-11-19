def password(str):
    pesan = ""
    if len(str) < 8:
        kurang_panjang = True
    else:
        kurang_panjang = False

    kurang_digit = True
    kurang_upper = True
    kurang_lower = True

    for i in range(0, len(str)):
        if str[i].isupper():
            kurang_upper = False
        elif str[i].islower():
            kurang_lower = False
        elif str[i].isdigit():
            kurang_digit = False

    if kurang_panjang:
        pesan += "not long enough"
    
    if kurang_digit:
        pesan += "\nno digit"
    
    if kurang_upper:
        pesan += "\nno uppercase"
    
    if kurang_lower:
        pesan += "\nno lowercase"

    print(pesan)

password_anda = input("Masukkan pass: ")
password(password_anda)