def remove_comma(kalimat):

    convert = list(kalimat)

    for i in range(0, len(convert)):
        if convert[i] == ",":
            convert[i] = "."

    hasil = ""
    return hasil.join(convert)
 
s = "nomor 1, nomor 2, nomor 3,"
result = remove_comma(s)
print("Before: ", s)
print("After: ", result)