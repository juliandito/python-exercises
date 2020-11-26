def costumer_record(fh, n):
    result = []
    for i in range(0, n):
        read = fh.readline()
        if i+1 == n:
            result = read.replace("\n","").split(",")

    return result


#bikin path ke direktori file
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'costumers.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "r")
print(costumer_record(f, 2))