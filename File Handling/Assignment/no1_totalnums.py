def total_nums(fh):
    list_string = fh.readline().split(" ")
    list_angka = []
    total = 0
    for i in range(0, len(list_string)):
        if list_string[i].isdigit():
            list_angka.append(list_string[i])
            total += int(list_string[i])
    
    return list_angka, total

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'text_numbers.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r")
result = total_nums(f)
print("List angka: ", result[0])
print("Total: ", result[1])