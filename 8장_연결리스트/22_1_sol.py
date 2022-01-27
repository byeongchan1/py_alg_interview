# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # index를 stack 하자!
        stack = []
        
        # answer 먼저 세팅하기. list에 * 연산은 복제
        answer = [0] * len(temperatures)
        
        
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack[-1]
                stack.pop()
                
                answer[last] = i - last
            
            stack.append(i)
        return answer