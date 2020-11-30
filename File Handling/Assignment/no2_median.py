def locate_median(fh):
    line_string = ""
    
    for line in fh:
        line_string += line.replace("\n"," ")
    
    list_skor_string = line_string.split(" ")
    list_skor_int = []

    for i in range(0, len(list_skor_string)):
        list_skor_int.append(int(list_skor_string[i]))

    sorted_list = sorted(list_skor_int)

    if len(sorted_list) % 2 != 0:
        median = sorted_list[int((len(list_skor_string)/2 - 0.5))]
    else:
        median = sorted_list[(len(list_skor_string)/2)]
    
    return median

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'numbers.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r")
result = locate_median(f)
print("List angka: ", result)