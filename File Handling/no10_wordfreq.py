def count_word_freq(fh, val):
    val_count = 0

    for line in fh:
        kata = line.replace("\n","")
        if kata == val:
            val_count+=1

    return val_count

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'words.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r")
dicari = "Exercise"
print("Word to search: ", dicari)
print(dicari, " appears ", count_word_freq(f, dicari), "time(s)")