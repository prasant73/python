def decimal_round_off(n):
    whole = n // 1
    print(whole)
    decimal = n - whole
    print(decimal)
    i = 0
    for i in range(2):
        decimal *= 10
        dec2 = decimal - (decimal // 1)
    if dec2 >= 0.5:
        decimal += 1
        decroundup = ((decimal // 1)) / 100
        num1 = whole + decroundup
        print("The rounded off decimal is:", num1)
    elif dec2 < 0.5:
        decrounddown = ((decimal // 1)) / 100
        num2 = whole + decrounddown
        print("The rounded off decimal is:", num2)
    

n = float(input("Enter the decimal number: "))
decimal_round_off(n)