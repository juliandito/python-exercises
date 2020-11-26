def find_longest(fh):
    longest_count = 0
    for line in fh:
        string_line = line.replace("\n","")
        list_line = list(string_line)
        if len(list_line) >= longest_count:
            longest_count = len(list_line)
            longest_word = string_line
    
    return longest_word

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'words.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r")
print("Longest: ", find_longest(f))