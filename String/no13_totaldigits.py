def total_digit(s):
    total = 0
    for i in range(0, len(s)):
        if s[i].isdigit():
            total += int(s[i])
            
    return total

print(total_digit("halo 1 halo 2 halo 25"))