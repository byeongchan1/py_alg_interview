# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

import collections
from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)

        left = start = end = 0

        # 오른쪽 포인터를 이동해보자
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            # 필요문자가 0개이면 왼쪽 포인터 이동해보자
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]
