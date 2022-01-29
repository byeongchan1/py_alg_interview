# 316. Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/

# Given a string s, remove duplicate letters so that every letter appears once and only once. 
# You must make sure your result is the smallest in lexicographical order among all possible results.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        # seen은 넣었다 안넣었다 체크용
        
        for char in s:
            counter[char] -= 1
            
            # 봤다면 다른 char 진행
            if char in seen:
                continue
                
            # stack 마지막 부분 char와 비교하여 제외
            # char 조건은 1) stack[-1] 보다 빠른지 2) stack[-1]이 뒤에서 또 나오는지
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())           
            
            stack.append(char)
            seen.add(char)
            
        return ''.join(stack)