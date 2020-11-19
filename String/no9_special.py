def special_count(s):
    count = 0
    for i in range(0, len(s)):
        if (s[i].isalnum() is not True) and (s[i].isspace() is not True):
            count += 1
    
    return count

print(special_count("halo 1 #@$&! halo 2 halo 333"))