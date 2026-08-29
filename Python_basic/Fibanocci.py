def fibonacci(n):
    a= 0
    b=1
    for i in range(n):
        print(a,end=" ")
        a,b = b,a+b

fibonacci(10)


# using recursion

# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1) + fib(n-2)

# n = 10
# for i in range(n):
#     print(fib(i),end = " ")
