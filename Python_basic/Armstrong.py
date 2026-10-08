def Armstrong(num:int)->bool:
    temp = num
    sum = 0
    length=len(str(num))
    while temp >0:
        digit = temp %10
        sum = sum + (digit**length)
        temp//=10

    if sum == num:
        return True
    else:
        return False

print(Armstrong(153))

