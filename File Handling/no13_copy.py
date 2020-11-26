def file_copy(fh1, fh2):
    
    for line in fh1:
        fh2.write(line)

    print("data appended to file")
    fh2.close()


#bikin path ke direktori file
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'words.txt')

# di open trus di jadiin params
# n itu line yang pengen dibaca
f1 = open(filename, "r")
f2 = open('new_words.txt', "a+")
file_copy(f1, f2)