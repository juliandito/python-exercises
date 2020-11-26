def costumer_best(fh):
    max_balance = 0.0
    result = []
                        # iterator buat ngecek posisi
    jumlah_lines = sum(1 for line in fh)    # cari jumlah lines, dipisah dari while pencarian biar hemat memori
    fh.seek(0) 

    for i in range(1, jumlah_lines):
        read = fh.readline()
        read_result = read.replace("\n","").split(",")
        balance = float(read_result[3])
        if balance > float(max_balance):
            max_balance = balance
            result = read_result
        
    return result


#bikin path ke direktori file
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'costumers.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r+")
print(costumer_best(f))