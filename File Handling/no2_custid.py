def costumer_id(fh, idc):
    result = []
    loop_pencarian = True

    iterator = 1                            # iterator buat ngecek posisi
    jumlah_lines = sum(1 for line in fh)    # cari jumlah lines, dipisah dari while pencarian biar hemat memori
    fh.seek(0)                              # balikin posisi jadi 0 lagi

    while loop_pencarian:
        read = fh.readline()
        read_result = read.replace("\n","").split(",")

        if int(read_result[0]) == idc:
            loop_pencarian = False
            result = read_result
        elif iterator == jumlah_lines:
            loop_pencarian = False
        
        iterator += 1                       # ditambah tiap looping biar nggak infinite loop

    return result

#bikin path ke direktori file
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'costumers.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r")
print(costumer_id(f, 234546))