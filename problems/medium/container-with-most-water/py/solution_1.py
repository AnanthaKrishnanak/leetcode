def maxArea(height):
    left = 0
    length = len(height)
    right = length
    result = 0

    while left <= length:
        right = length - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > result:
                result = area
            right -= 1

        left += 1

    return result


def run_tests():
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 25),
        ([0, 0, 0, 10, 0, 0, 0], 0),
        ([5, 5, 5, 5, 5, 5, 5, 5], 35),
        ([0, 1], 0),
        ([4, 3, 2, 1, 4], 16),
    ]

    for i, (height, expected) in enumerate(test_cases, 1):
        result = maxArea(height)
        print(
            f"Testcase {i}: Input={height} | Expected={expected} | Got={result} | {'PASS' if result == expected else 'FAIL'}"
        )


run_tests()
