def missingNumber(nums):
    length = len(nums)
    total_sum = length * (length + 1) // 2
    return total_sum - sum(nums)
