def Postfix_Expression(expression):
    stack = []
    postfix = []
    precedency = {
                '+': 1,
                '-': 1,
                '*': 2,
                '/': 2,
                '^': 3
                }
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char.isalnum():
            postfix.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and precedency[stack[-1]] >= precedency[char]):
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())
    return "".join(postfix)

expression = "(A+B)*C+D/(B+A*C)+D"
print(Postfix_Expression(expression))