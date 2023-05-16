# https://leetcode.com/problems/add-binary/
# 67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:  # 63ms
        res = ""
        a_rev = a[::-1]
        b_rev = b[::-1]
        carry = 0

        for i in range(max(len(a), len(b))):
            bit_a = int(a_rev[i]) if i < len(a_rev) else 0
            bit_b = int(b_rev[i]) if i < len(b_rev) else 0
            total = bit_a + bit_b + carry

            char = str(total % 2)
            res = char + res
            carry = total // 2

        if carry:
            res = "1" + res

        return res


if __name__ == '__main__':
    tests = [
        ["11", "1", "100"],
        ["1010", "1011", "10101"]
    ]

    sol = Solution()
    for test in tests:
        result = sol.addBinary(test[0], test[1])

        if result == test[2]:
            print(result)
        else:
            print(f"Error: Expected { test[2] } but got { result } instead for { test[0] } and { test[1] }")
