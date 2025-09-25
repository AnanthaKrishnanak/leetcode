def rotate(nums, k):
    p = len(nums) - 1
    for i in range(k):
        temp = nums[p]
        for k in range(p, 0, -1):
            nums[k] = nums[k - 1]
        nums[0] = temp

    return nums


print(rotate([-1, -100, 3, 99], 2))
print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
