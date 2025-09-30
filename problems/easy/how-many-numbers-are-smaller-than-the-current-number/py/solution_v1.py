def smallerNumbersThanCurrent(nums):
    res = []
    i = 0
    while i < len(nums):
        c = 0
        for n in nums:
            if n < nums[i]:
                c += 1
        i += 1
        res.append(c)
    return res
