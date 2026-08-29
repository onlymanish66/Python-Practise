def Armstrong(num):
    temp = num
    length = 0
    sum = 0
    while temp > 0:
        length+=1
        temp //=10

    temp = num
    while temp >0:
        digit = temp %10
        sum = sum + (digit**length)
        temp//=10

    if sum == num:
        return True
    else:
        return False

print(Armstrong(153))

