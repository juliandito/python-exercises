def remove_vowel(kalimat):

    vowel = "AaIiUuEeOo"
    hasil = kalimat
    for i in range(0, len(vowel)):
        hasil = hasil.replace(vowel[i],"")

    return hasil
 
s = "I think your book is an utter garbage"
result = remove_vowel(s)
print("Before: ", s)
print("After: ", result)