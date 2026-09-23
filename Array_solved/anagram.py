" using built in functions "
def anagram(str1 : str , str2 : str) -> bool: # str tells that parameters value should be string
    clear1 = "".join(str1.lower().split())      # bool tells that function return boolean value
    clear2 = "".join(str2.lower().split())   # split use to remove multiple spaces from string
    return sorted(clear1) == sorted(clear2)


print(anagram("silent","list en"))



" using without built in functions "

# def anagram(str1:str,str2)->bool:
#     count = [0]*256    #maximum  range of string ascii value 
#     for ch in str1:
#         val = ord(ch)   # calculate ascii value
#         if val == 32 or val == 9 or val == 10:    # skip spaces
#             continue
#         if 65>=val<=90:    # convert capital letter into small letter
#             val+=32
#         count[val]+=1   #val ke index par 1 add krte rhenge

#     for ch in str2:
#             val = ord(ch)   # calculate ascii value
#             if val == 32 or val == 9 or val == 10:    # skip spaces
#                 continue
#             if 65>=val<=90:    # convert capital letter into small letter
#                 val+=32
#             count[val]-=1   #val ke index par 1 minus krte rhenge kyoki sab par
#                             #  0 ho jaayega yaani letter same hai
#     for c in count:
#         if c != 0:
#             return False
#     return True

# print(anagram("silent","lis ten"))


" if string list is given and tell no. of different anagrams group"
" ex = [tea,eat,silent,listen,bat,tab] so total 3 different groups"

# def anagram(stringlist):
#     group = {}  #total kitne different anagram tuple honge
#     for str in stringlist:
#         count = [0]*256

#         for ch in str:
#             val = ord(ch)   # calculate ascii value
#             if val == 32 or val == 9 or val == 10:    # skip spaces
#                 continue
#             if 65>=val<=90:    # convert capital letter into small letter
#                 val+=32
#             count[val]+=1   #val ke index par 1 add krte rhenge
#         count_tuple = tuple(count)   # kyoki dict list ko as a key nhi store krti

#         if count_tuple not in group:
#             group[count_tuple] = True
#     return len(group)

# strlist = ["silent","eat","listen","tea","tab"]
# print(anagram(strlist))

        