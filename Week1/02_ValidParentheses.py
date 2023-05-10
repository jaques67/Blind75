# https://leetcode.com/problems/valid-parentheses/
# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:  # 42ms
        if len(s) % 2 != 0:
            return False
        matching_paren = {'}': '{', ']': '[', ')': '('}
        open_paren = ['[', '{', '(']
        stack = []

        for letter in s:
            if letter in open_paren:
                stack.append(letter)
                continue
            if stack:
                top = stack.pop()
            else:
                return False

            if matching_paren[letter] != top:
                return False

        return not stack


if __name__ == '__main__':
    tests = [
        ["()", True],
        ["()[]{}", True],
        ["(]", False]
    ]
    sol = Solution()
    for test in tests:
        output = sol.isValid(test[0])
        if output == test[1]:
            print(output)
        else:
            print(f"Error: Expected { test[1] } but got { output } instead for { test[0] }")
