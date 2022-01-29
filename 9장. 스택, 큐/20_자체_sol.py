# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        stack_1 = []

        for _ in s:
            if _ == '(':
                stack_1.append(1)
            if _ == ')':
                if not stack_1:
                    return False
                else:
                    if stack_1[-1] != 1:
                        return False
                    else:
                        stack_1.pop()
            
            if _ == '[':
                stack_1.append(2)
            if _ == ']':
                if not stack_1:
                    return False
                else:
                    if stack_1[-1] != 2:
                        return False
                    else:
                        stack_1.pop()
            
            if _ == '{':
                stack_1.append(3)
            if _ == '}':
                if not stack_1:
                    return False
                else:
                    if stack_1[-1] != 3:
                        return False
                    else:
                        stack_1.pop()
        
        if not stack_1:
            return True
                    
        
            
            