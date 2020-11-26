def count_freq(fh, val):
    val_count = 0
    for line in fh:
        if int(line) == val:
            val_count+=1

    return val_count

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'numbers.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r")
print("count of 9:" , count_freq(f, 9))