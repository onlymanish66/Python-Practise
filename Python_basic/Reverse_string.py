def Reverse_string(s):
    s = list(s)
    left = 0
    right = len(s)-1
    while left<right:
        s[left],s[right] = s[right],s[left]
        left+=1
        right-=1
    res = "".join(s)
    return res

s = "manish"
res = Reverse_string(s)
print(res)