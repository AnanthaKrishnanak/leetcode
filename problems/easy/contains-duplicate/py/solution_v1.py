def containsDuplicate(nums):
    seen = {}
    for n in nums:
        if seen.get(n) != None:
            return True
        seen[n] = n
    return False

#first attempt
#solved in 2 min