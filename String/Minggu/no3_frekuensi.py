def frequency(input_str):
    all_freq = {}               #init dictionary, nyimpen huruf sama freq tiap huruf
    for i in input_str:         
        if i in all_freq:       #cek karakteerr udah ada di dict belum
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    
    highest_freq = max(all_freq.values()) #cari max valuenya
    highest_freq_char = []     
    for freq_char, freq in all_freq.items():    #cari huruf yang punya value = highest_freq
        if freq == highest_freq:
            highest_freq_char.append(freq_char)

    return highest_freq_char[0]                    

stringInput = input("Masukkan string: ")
print("Most freq: ", frequency(stringInput))

