# https://leetcode.com/problems/majority-element/
# 169. Majority Element
import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:  # 166ms
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        key, val = None, -1
        for k, v in counts.items():
            if v > val:
                key = k
                val = v
        return key

    def majorityElement_hashmap(self, nums: List[int]) -> int:  # 171ms
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


if __name__ == '__main__':
    tests = [
        [[3, 2, 3], 3],
        [[2, 2, 1, 1, 1, 2, 2], 2]
    ]

    sol = Solution()
    for test in tests:
        # output = sol.majorityElement(test[0])
        output = sol.majorityElement_hashmap(test[0])
        if output == test[1]:
            print(output)
        else:
            print(f"Error: Expected { test[1] } but got { output } instead for { test[0] }")
