# 문제
# 주어진 문자열이 팰린드롬인지 확인하라.
# 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

# https://leetcode.com/problems/valid-palindrome/

import collections
from typing import Deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 리스트로 변환
        # s의 한글자 한글자에 대하여 알파벳인지, 숫자인지 판단하고 list에 추가
        
        # 자료형 데크로 선언
        strs : Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬인지 판단하기
        # str.pop() method는 인덱스를 지정할 수 있기 때문에, 0을 지정하면 맨 앞의 값을 가져오면서 list에서 삭제한다
        while len(strs) > 1:
            if strs.popleft() != strs.pop(): # Deque의 popleft는 O(1)
                return False
        return True
    
    # Runtime : 61ms, MEM : 19.2MB