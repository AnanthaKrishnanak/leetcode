def rotate(nums, k):
    n = len(nums)
    k %= n
    if k == 0:
        return nums

    nums[:] = nums[-k:] + nums[:-k]
    return nums


print(rotate([-1, -100, 3, 99], 2))
print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
