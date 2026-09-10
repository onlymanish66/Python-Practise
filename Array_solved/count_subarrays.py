def count_subarrays(nums,k):
    coun = 0
    prefix_sum = 0
    freq = {0:1}
    for num in nums:
        prefix_sum+=num
        if (prefix_sum-k) in freq:
            coun+=freq[prefix_sum-k]  # count+=1 also
        if prefix_sum not in freq:
            freq[prefix_sum] = 1
        else:
            freq[prefix_sum]+=1
    return coun

nums = [9,4,20,3,10,5,33]
k = 33
print(count_subarrays(nums,k))