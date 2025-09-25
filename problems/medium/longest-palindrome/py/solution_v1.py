def isPalindrome(s: str):
    i, l = 0, len(s) - 1
    while l >= 0:
        if s[i] != s[l]:
            return False
        i += 1
        l -= 1
    return True


def longestPalindrome(s: str):
    length = len(s)
    left, right = 0, length
    result = ""

    while left < length:
        right = length
        result_length = len(result)
        if result_length >= right - left:
            break
        while left < right:
            sub = s[left:right]

            if isPalindrome(sub):
                if len(result) < len(sub):
                    result = sub

            right -= 1

        left += 1

    return result


# Improvements made to brute force approach:
# - Added caching to avoid rechecking substrings
# - Still run into time exceeded with larger input
# - Added check to  skip iterations if the current longest palindrome is longer than the substring being checked
# - caching was unnecessary for this problem - removed caching
# - current solution complexity is O(n^3)
#- to optimize - > https://www.geeksforgeeks.org/dsa/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/