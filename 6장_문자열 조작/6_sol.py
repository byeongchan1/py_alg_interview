# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팬린드롬 판단 및 두 포인트 확장하기
        def expension(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
            
        # 해당사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        # 슬라이딩 윈도우로 우측으로 이동
        # max함수는 끝에 함수를 기준으로 max 구할 수 있음 (lambda 함수 사용 가능)
        for i in range(len(s) - 1):
            result = max(result,
                        expension(i, i+1),
                        expension(i, i+2),
                        key=len)
        return result