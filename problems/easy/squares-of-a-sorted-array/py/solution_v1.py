class Solution(object):
    def sortedSquares(self, nums):
        sorted_squares = [0 for _ in range(len(nums))]
        l = 0
        r = len(nums) - 1
        i = len(nums) - 1
        while r >= l:
            if abs(nums[r]) > abs(nums[l]):
                sorted_squares[i] = nums[r] ** 2
                r -= 1
            else:
                sorted_squares[i] = nums[l] ** 2
                l += 1
            i -= 1
        return sorted_squares
