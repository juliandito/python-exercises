def calculate(expr):
    x = expr.split()

    result = 0
    if x[1] == "+":
        result = int(x[0]) + int(x[2])
    elif x[1] == "-":
        result = int(x[0]) - int(x[2])
    elif x[1] == "*":
        result = int(x[0]) * int(x[2])
    elif x[1] == "%":
        result = int(x[0]) % int(x[2])
    elif x[1] == "/":
        if x[2] == "0":
            result = None
        else:
            result = int(x[0]) / int(x[2])
            

    return result

print( calculate("10 / 5"))