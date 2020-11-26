def find_short(fh):

    string_line = fh.readline().replace("\n","")
    list_line = list(string_line)
    short_count = len(list_line)
    fh.seek(0)

    for line in fh:
        string_line = line.replace("\n","")
        list_line = list(string_line)
        if len(list_line) <= short_count:
            short_count = len(list_line)
            short_word = string_line
    
    return short_word

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'words.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r")
print("Shortest: ", find_short(f))