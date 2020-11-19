def vowel_count(s):
    converted_str =  s.lower()
    count =  converted_str.count("a") + converted_str.count("i") + converted_str.count("u") + converted_str.count("e") + converted_str.count("o") 
    return count

total = vowel_count("aiueoyAA")
print(total)