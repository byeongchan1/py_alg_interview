# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()

        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1

            max_char_n = counts.most_common(1)[0][1]
            
            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right - left