def char_frequency(s):
    s = s.lower()
    count={}
    for char in s:
        if char not in count:
            count[char] =1
        else:
            count[char]+=1
    return count

s = "Manish Agrawal"
print(char_frequency(s))
    