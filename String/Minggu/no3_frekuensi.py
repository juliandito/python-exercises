def frequency(input_str):
    all_freq = {}               #init dictionary, nyimpen huruf sama freq tiap huruf
    for i in input_str:         
        if i in all_freq:       #cek karakteerr udah ada di dict belum
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    
    highest_freq = max(all_freq.values())       #cari max valuenya
    for freq_char, freq in all_freq.items():    #cari huruf yang punya value = highest_freq
        if freq == highest_freq:
            highest_freq_char = freq_char
            break                               #kalo udah ketemu satu langsung berhenti

    return highest_freq_char                    

stringInput = input("Masukkan string: ")
print("Most freq: ", frequency(stringInput))

