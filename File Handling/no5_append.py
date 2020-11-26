def costumer_append(fh, field):
    input_data = "\n" + ','.join(map(str, field))
    fh.write(input_data)
    print("data appended to file")
    fh.close()


#bikin path ke direktori file
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'costumers.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f = open(filename, "a")
field = ["35612", "David", "Brown", "237.56", "2008-10-10"]
print("Data: ", field)
costumer_append(f, field)