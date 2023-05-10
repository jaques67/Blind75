# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[num] = i


if __name__ == '__main__':
    tests = [
        [[2, 7, 11, 15], 9, [0, 1]],
        [[3, 2, 4], 6, [1, 2]],
        [[3, 3], 6, [0, 1]]
    ]

    sol = Solution()
    for test in tests:
        output = sol.twoSum(test[0], test[1])
        if output == test[2]:
            print(output)
        else:
            print(f"Error: Expected { test[2] } but received { output } instead for: {test[0]}")
