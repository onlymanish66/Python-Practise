def check_Pallindrome(num):
    num = str(num)
    left = 0
    right = len(num)-1
    while left<right:
        if num[left]!=num[right]:
            return False
        left+=1
        right-=1
    return True

num = 110011
print(check_Pallindrome(num))