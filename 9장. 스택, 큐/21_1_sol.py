# 316. Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/

# Given a string s, remove duplicate letters so that every letter appears once and only once. 
# You must make sure your result is the smallest in lexicographical order among all possible results.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 재귀함수로 풀어보기
        # 집합으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            
            # 전체집합과 접미사 집합이 일치할때 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
            
        return ''