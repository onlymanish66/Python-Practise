def max_product_subarray(nums):
    max_prod = nums[0]
    cur_max = nums[0]
    cur_min = nums[0]
    for i in range(1,len(nums)):
        num = nums[i]
        if num<0:
            cur_max,cur_min = cur_min,cur_max
        cur_max = max(num,cur_max*num)
        cur_min = min(num,cur_min*num)
        max_prod = max(cur_max,max_prod)
    return max_prod

nums = [3,2,-2,3,1]
print(max_product_subarray(nums))