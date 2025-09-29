def missingNumber(nums):
    for i in range(max(nums) + 1):
        if i not in nums:
            return i
    return max(nums) + 1
