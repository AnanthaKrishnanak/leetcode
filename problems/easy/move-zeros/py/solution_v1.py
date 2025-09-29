def move_zeros(nums):
    k = 0
    i = 0
    l = len(nums) - 1
    while i <= l:
        if k == l:
            break
        if nums[k] != 0:
            k += 1

        if nums[i] != 0 and k <= i:
            nums[k] = nums[i]
            nums[i] = 0
            i += 1
            k += 1
        else:
            i += 1
            
# brute force
