def factorial(num):
    if num ==1 or num ==0:
        return 1
    return factorial(num-1)*num

print(factorial(5))