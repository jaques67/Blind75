# https://leetcode.com/problems/first-bad-version/
# 278. First Bad Version
# AlgoMonster: Under Binary Search/Overview: https://algo.monster/problems/binary_search_boundary
# Simple Binary Search for first True

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

    def __init__(self, bad):
        self.bad = bad

    def firstBadVersion(self, n: int) -> int:  # 45ms
        low, high = 0, n
        first = -1
        while low <= high:
            mid = low + (high - low) // 2
            result = self.isBadVersion(mid)
            if result:
                first = mid
                high = mid - 1
            else:
                low = mid + 1
        return first

    def isBadVersion(self, version):
        return version == self.bad


if __name__ == '__main__':
    tests = [
        [5, 4, 4],
        [1, 1, 1]
    ]

    for test in tests:
        sol = Solution(test[1])
        output = sol.firstBadVersion(test[0])

        if output == test[2]:
            print(output)
        else:
            print(f"Error: Expected { test[2] } but got { output } instead for: { test[0] }")
