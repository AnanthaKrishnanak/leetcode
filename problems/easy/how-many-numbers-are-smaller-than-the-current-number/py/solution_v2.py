def smallerNumbersThanCurrent(nums):
    temp = sorted(nums)
    map = {}
    res = []
    for index, num in enumerate(temp):
        if num not in map:
            map[num] = index
    for num in nums:
        res.append(map[num])
    return res
