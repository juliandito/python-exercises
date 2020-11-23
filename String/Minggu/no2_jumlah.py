def sum_digits(s):
    total = 0
    for i in range(0, len(s)):
        if s[i].isdigit():
            total += int(s[i])
            
    return total

print(sum_digits("2501"))