# https://leetcode.com/problems/ransom-note/
# 383. Ransom Note
# AlgoMonster: Under backtracking/Additional States/All permutations: https://algo.monster/problems/permutations
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:  # 101ms
        if len(ransomNote) > len(magazine):
            return False

        a = ord('a')
        rn = [0] * 26
        mn = [0] * 26
        for i in range(len(ransomNote)):
            rn[ord(ransomNote[i]) - a] += 1
        for i in range(len(magazine)):
            mn[ord(magazine[i]) - a] += 1

        for i in range(len(rn)):
            if rn[i] == 0:
                continue
            if rn[i] > mn[i]:
                return False

        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:  # 50ms
        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char, "", 1)
            else:
                return False

        return True

    def canConstruct2a(self, ransomNote: str, magazine: str) -> bool:  # 106ms
        # mn = sorted(magazine)
        mn = "".join(sorted(magazine))
        for char in ransomNote:
            if char in mn:
                mn = mn.replace(char, "", 1)
            else:
                return False

        return True

    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:  # 125ms
        sn_sorted = sorted(ransomNote)
        mn_sorted = sorted(magazine)
        i, j = 0, 0
        ransomNote_length = len(ransomNote)
        magazine_length = len(magazine)
        a = ord('a')

        while i < ransomNote_length and j < magazine_length:
            s_letter = ord(sn_sorted[i])
            m_letter = ord(mn_sorted[j])
            if s_letter == m_letter:
                i += 1
                j += 1
                continue
            if s_letter < m_letter:  # no more letters
                return False
            else:
                while m_letter < s_letter and j < magazine_length:
                    j += 1
                    if j < magazine_length:
                        m_letter = ord(mn_sorted[j])

                if j >= magazine_length:
                    return False

                if s_letter < m_letter:
                    return False
                if s_letter == m_letter:
                    i += 1
                    j += 1
                    continue
        if i < ransomNote_length:
            return False
        else:
            return True


if __name__ == '__main__':
    tests = [
        ["a", "b", False],
        ["aa", "ab", False],
        ["aa", "aab", True],
        ["fihjjjjei", "hjibagacbhadfaefdjaeaebgi", False],
        ["az", "ab", False]
    ]

    sol = Solution()
    for test in tests:
        # output = sol.canConstruct(test[0], test[1])
        output = sol.canConstruct2(test[0], test[1])
        # output = sol.canConstruct3(test[0], test[1])
        # output = sol.canConstruct2a(test[0], test[1])

        if output == test[2]:
            print(output)
        else:
            print(f"Error: Expected { test[2] } but got { output } instead for: { test[0] }:{ test[1] }")
