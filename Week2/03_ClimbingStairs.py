# https://leetcode.com/problems/climbing-stairs/
# 70. Climbing Stairs
# AlgoMonster:
# Dynamic Programming - Bottom up
class Solution:
    def climbStairs(self, n: int) -> int:  # 42ms
        one, two = 1, 1

        for i in range(n - 1):
            # temp = one
            # one = one + two
            # two = temp
            one, two = one + two, one

        return one


if __name__ == '__main__':
    tests = [
        [2, 2],
        [3, 3]
    ]

    sol = Solution()
    for test in tests:
        output = sol.climbStairs(test[0])

        if output == test[1]:
            print(output)
        else:
            print(f"Error: Expected { test[1] } but got { output } instead for { test[0] }")
