def costumer_first(fh):
    earliest = "2020-11-26"
    result = []

    jumlah_lines = sum(1 for line in fh)    # cari jumlah lines, dipisah dari while pencarian biar hemat memori
    fh.seek(0) 

    for i in range(1, jumlah_lines):
        read = fh.readline()
        read_result = read.replace("\n","").split(",")
        date = read_result[4]
        if date < earliest:
            earliest = date
            result = read_result
        
    return result

#bikin path ke direktori file
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'costumers.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r+")
print(costumer_first(f))