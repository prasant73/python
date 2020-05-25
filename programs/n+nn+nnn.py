def sum_series(n):
    sum = 0
    b = 0
    # for i in range(3):
    #     if i == 0:
    #         sum = b = n
    #     else:
    #         b = b * 10 + n # 55, 
    #         sum = sum + b
    count = 0
    while (count < 3):
        if count == 0:
            sum = b = n
            count += 1
        else:
            b = b * 10 + n # 55, 
            sum = sum + b
            count += 1
    return sum
print(sum_series(5))

'''
    a = 5
    a = 5  * 10 + 5 = 55; sum = sum + a
    55 * 10 + 5 = 555

'''