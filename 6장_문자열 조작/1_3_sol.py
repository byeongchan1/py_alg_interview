# 문제
# 주어진 문자열이 팰린드롬인지 확인하라.
# 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

# https://leetcode.com/problems/valid-palindrome/

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # 'a man, a plan, a canal: panama'

        s = re.sub('[^a-z0-9]', '', s) # 정규식을 이용해서 원하는 것 빼고 모두 ''처리 / 'amanaplanacanalpanama'

        return s == s[::-1] # str 슬라이싱 이용
    
    # Runtime : 61ms, MEM : 19.2MB