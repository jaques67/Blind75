# https://leetcode.com/problems/valid-palindrome/
# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:  # 64ms
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == '__main__':
    tests = [
        ["A man, a plan, a canal: Panama", True],
        ["race a car", False]
    ]

    sol = Solution()
    for test in tests:
        output = sol.isPalindrome(test[0])

        if output == test[1]:
            print(output)
        else:
            print(f"Error: Expected {test[1]} but got {output} instead for {test[0]}")
