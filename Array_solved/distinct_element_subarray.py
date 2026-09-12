    def Distinct_element_subarray(nums):
        seen = {}
        max_length = 0
        left = 0
        for i in range(len(nums)):
            if nums[i] in seen:
                left = max(left,seen[nums[i]]+1)
            seen[nums[i]] = i
            length = i - left+1
            max_length = max(max_length,length)

        return max_length

    nums = [1,2,6,2,1,3,4]
    print(Distinct_element_subarray(nums))
