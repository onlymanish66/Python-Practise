def longest_subarray(nums,k):
    max_length = 0
    seen = {0:-1}
    prefix_sum = 0
    for i in range(len(nums)):
        prefix_sum+=nums[i]
        target = prefix_sum-k
        if target in seen:
            length = i - seen[target]
            max_length =max(length,max_length)
        if prefix_sum not in seen:
            seen[prefix_sum] = i
    return max_length

nums = [1,-1,5,-2,3]
k = 3
print(longest_subarray(nums,k))