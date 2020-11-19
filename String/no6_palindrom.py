def is_palindrome(kalimat):
    return kalimat == kalimat[::-1]
 
 
s = "kasurusak"
result = is_palindrome(s)
 
if result:
    print("Yes")
else:
    print("No")