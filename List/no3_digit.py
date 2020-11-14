def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    DG0 = "zero"
    DG1 = "one"
    DG2 = "two"
    DG3 = "three"
    DG4 = "four"
    DG5 = "five"
    DG6 = "six"
    DG7 = "seven"
    DG8 = "eight"
    DG9 = "nine"
    mylist = [
        DG0,
        DG1,
        DG2,
        DG3,
        DG4,
        DG5,
        DG6,
        DG7,
        DG8,
        DG9,
    ]
    return mylist[n]


for i in range (0, 10):
    print(get_digit_name(i))