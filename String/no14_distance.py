def str_distance(s1, s2):

    if len(s1) == len(s2):
        diff_count = 0
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                diff_count += 1
        
        if diff_count == 0:
            d = 0
        else:
            d = diff_count

    else:
        d = -1

    return d

print(str_distance("David", "David"))