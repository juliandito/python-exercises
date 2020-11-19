def digit_count(s):
    count = 0
    for i in range(0, len(s)):
        if s[i].isdigit():
            count += 1
    
    return count

print(digit_count("halo 1 halo 2 halo 333"))