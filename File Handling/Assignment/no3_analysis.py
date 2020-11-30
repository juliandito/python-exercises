def fine_analysis(fh):

    count_uppercase = 0
    count_lowercase = 0
    count_digits = 0
    count_space = 0

    for line in fh:
        string_list = list(line.replace("\n"," "))
        for i in range(0, len(string_list)):
            if string_list[i].isupper():
                count_uppercase += 1
            elif string_list[i].islower():
                count_lowercase += 1
            elif string_list[i].isdigit():
                count_digits += 1
            elif string_list[i].isspace():
                count_space += 1
    
    return count_uppercase, count_lowercase, count_digits, count_space

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'text.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r")
result = fine_analysis(f)
print("Upper: ", result[0])
print("Low: ", result[1])
print("Digit: ", result[2])
print("Space: ", result[3])