def Existence_of_zero_sum_subarray(nums):
    seen= {0}
    prefix_sum = 0
    for num in nums:
        prefix_sum+=num
        if prefix_sum in seen:
            return "Exist"
        seen.add(prefix_sum)
    return "Not Exist"

nums = [2,3,-2,-1,3]
print(Existence_of_zero_sum_subarray(nums))
