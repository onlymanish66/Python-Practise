def Max_sum_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    for i in range (1,len(nums)):
        current_sum+=nums[i]
        current_sum = max(nums[i],current_sum)
        max_sum = max(current_sum,max_sum)

    return max_sum

nums = [-2,1,-3,4,-1,2]
print(Max_sum_subarray(nums))
