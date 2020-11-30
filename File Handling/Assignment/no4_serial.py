def is_valid(fh):
    result_all = []

    for line in fh:
        status_all = True
        result_per_line = []
        status_line = []
        result_per_line.append(line.replace("\n",""))
        line_string_list = list(line.replace("\n",""))
        
        if len(line_string_list) != 11:
            status_line.append(False)

        if line_string_list[0] != "S" and line_string_list[1] != "N":
            status_line.append(False)
        
        if line_string_list[2] != "/":
            status_line.append(False)
        
        for i in range(3, 7):
            if line_string_list[i].isdigit==False:
                status_line.append(False)

        if line_string_list[7] != "-":
            status_line.append(False)

        flag_false = 0
        for item in status_line:
            if item == False:
                    flag_false += 1
    
        if flag_false != 0:
            status_all = False

        result_per_line.append(status_all)
        result_all.append(result_per_line)

    return result_all

import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'serial_number.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r")
result = is_valid(f)
for i in range(0, len(result)):
    print("Seri: ", result[i][0], " adalah ", result[i][1])
