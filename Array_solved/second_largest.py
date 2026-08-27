def sec_largest(arr):
    largest =float("-inf")          # -infinity smallest number, to compare with -ve numbers.
    second_largest = float("-inf")
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return largest,second_largest

arr = [-1,-2,-4,-7,-3]
largest,second_largest = sec_largest(arr)
print("Largest = ",largest,"second_largest = ",second_largest)

