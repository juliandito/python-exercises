def append_increment(fh):

    jumlah_lines = sum(1 for line in fh)    # cari jumlah lines, dipisah dari while pencarian biar hemat memori
    fh.seek(0) 

    for i in range(1, jumlah_lines):
        angka = fh.readline()
        if i == jumlah_lines-1:
            last = int(angka) + 1
    
    fh.write("\n" + str(last))
    
    print(last, " is appended")

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'numbers.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r+")
append_increment(f)