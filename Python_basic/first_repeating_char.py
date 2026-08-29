# def first_repeating(s):
#     seen=[]
#     s = s.lower()
#     for i in s:
#         if i in seen:
#             return i
#         else:
#             seen.append(i)

# s = "abCdEfghc"
# print(first_repeating(s))

def first_non_repeating_char(s):
    s = s.lower()
    seen ={}
    for i in s:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i]+=1

    for j in seen:
        if seen[j]==1:
            return j
    return "No character"

s = "aabbcdde"
print(first_non_repeating_char(s))
