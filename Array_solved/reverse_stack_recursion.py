def reverse_stack_recursion(stack,index):
    if index == len(stack)//2:
        return
    stack[index],stack[len(stack)-1-index]=stack[len(stack)-1-index],stack[index]
    reverse_stack_recursion(stack,index+1)

stack = [5,3,1,8,2]
reverse_stack_recursion(stack,0)
print(stack)

# def reverse_stack_recursion(stack,index):
#     if index==-1:
#         return
#     reverse_stack_recursion(stack,index-1)
#     if index<len(stack)-1-index:
#         stack[index],stack[len(stack)-1-index]=stack[len(stack)-1-index],stack[index]


# stack = [5,3,1,8,2]
# reverse_stack_recursion(stack,len(stack))
# print(stack)