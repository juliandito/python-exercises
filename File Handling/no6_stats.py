def number_stats(fh):
    
    total = 0 
    smallest = int(fh.readline())
    count = 1
    largest = 0
    total = 0

    for line in fh:
        angka = int(line)
        total += angka
        count += 1
        if angka > largest:
            largest = angka
        elif angka < smallest:
            smallest = angka
    
    return smallest, largest, total, total/count



#bikin path ke direktori file
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'numbers.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r+")
result = number_stats(f)
print("Smallest: ", result[0])
print("Largest: ", result[1])
print("Total: ", result[2])
print("Average: ", result[3])