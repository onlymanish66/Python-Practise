def valid_parantheses(s:str)->bool:
    if s=="":
        return False
    if s[0] in ")]}":
        return False
    stack = []
    hash = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    for i in s:
        if stack and i in ")]}":
            if hash[i] != stack[-1]:
                return False
            stack.pop()
        else:
            stack.append(i)

    if stack:
        return False
    else:
        return True

s = "([{([])}])"
print(valid_parantheses(s))