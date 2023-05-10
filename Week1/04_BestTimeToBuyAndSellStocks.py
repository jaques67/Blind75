# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 121. Best Time to Buy and Sell Stock
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:  # 993ms
        res = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)

        return res


if __name__ == '__main__':
    tests = [
        [[7, 1, 5, 3, 6, 4], 5],
        [[7, 6, 4, 3, 1], 0]
    ]

    sol = Solution()
    for test in tests:
        output = sol.maxProfit(test[0])

        if output == test[1]:
            print(output)
        else:
            print(f"Error: Expected { test[1] } but got { output } instead for { test[0] }")
