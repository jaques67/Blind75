# https://leetcode.com/problems/binary-search/
# 704. Binary Search
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:  # 248ms
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    tests = [
        [[-1, 0, 3, 5, 9, 12], 9, 4],
        [[-1, 0, 3, 5, 9, 12], 2, -1],
        [[5], 5, 0]
    ]

    sol = Solution()
    for test in tests:
        output = sol.search(test[0], test[1])

        if output == test[2]:
            print(output)
        else:
            print(f"Error: Expected { test[2] } but got { output } instead for: { test[0] }")
