# https://leetcode.com/problems/valid-anagram/
# 242. Valid Anagram
from collections import  Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  # 54ms
        # Not sure if this will be accepted in an interview
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

    def isAnagram2(self, s: str, t: str) -> bool:  # 65ms
        if len(s) != len(t):
            return False

        s_letters = [0] * 26
        t_letters = [0] * 26
        a = ord('a')
        for letter in s:
            s_letters[ord(letter) - a] += 1
        for letter in t:
            t_letters[ord(letter) - a] += 1

        return s_letters == t_letters

    def isAnagram3(self, s: str, t: str) -> bool:  # 78ms
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        return count_s == count_t


if __name__ == '__main__':
    tests = [
        ["anagram", "nagaram", True],
        ["rat", "car", False]
    ]

    sol = Solution()
    for test in tests:
        # output = sol.isAnagram(test[0], test[1])
        # output = sol.isAnagram2(test[0], test[1])
        output = sol.isAnagram3(test[0], test[1])

        if output == test[2]:
            print(output)
        else:
            print(f"Error: Expected { test[2] } but got { output } instead for: { test[0] } and { test[1] }")
