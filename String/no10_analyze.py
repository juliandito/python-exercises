def text_analyze(s):
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    for i in range(0, len(s)):
        if s[i].isdigit():
            dgts += 1
        elif s[i].isupper():
            uppr += 1
        elif s[i].islower():
            lowr += 1
        elif s[i] == " ":
            whtspc += 1
    
    return dgts, uppr, lowr, whtspc

result = text_analyze("halo 1234 TEST")

print("Digits: ", result[0])
print("Upper: ", result[1])
print("Lower: ", result[2])
print("Spaces: ", result[3])