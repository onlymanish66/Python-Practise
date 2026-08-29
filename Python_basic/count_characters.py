def count_characters(s):
    s = s.lower()
    vowels = 0
    consonants = 0
    digits = 0
    spaces = 0
    for i in s:
        if i in "aeiou":
            vowels+=1
        elif  'a'<=i<='z':
            consonants+=1
        elif '0'<=i<='9':
            digits+=1
        elif i ==" ":
            spaces+=1
    print("vowels = ",vowels,"consonants = ",consonants,"digits = ",digits,"spaces = ",spaces)

s = "heLlo my world 123"
count_characters(s)