def check_Pallindrome(s):
    s = s.lower()
    left = 0
    right = len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

s ="madaM"
print(check_Pallindrome(s))