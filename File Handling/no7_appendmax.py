def append_max_num(fh):

    largest = 0
    for line in fh:
        angka = int(line)
        if angka > largest:
            largest = angka
    
    fh.write("\n" + str(largest))
    
    print(largest, " is appended")

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'numbers.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r+")
append_max_num(f)