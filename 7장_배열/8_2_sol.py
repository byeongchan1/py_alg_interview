# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Stack 풀이
        # Stack은 LIFO (Last In First Out)
        # 여기서 stack으로 i를 쌓다가, 변곡점이 생기면 stack에서 빼낸다.
        
        stack = []
        volume = 0
        
        for i in range(len(height)):
            
            # python and 연산자
            # A and B : A 가 참일경우 B값 출력
            # A가 거짓일경우 A 값 출력
            # stack = [] 일경우 False
            # stack 안에 내용 있을경우 뒷 비교연산 처리됨
            
            # 변곡점을 만나는 경우
            
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()
                
                # len(stack) = 0 일 경우
                # 왜 멈추는지? -> 왼쪽 벽이 없기 때문
                if not len(stack):
                    break
                
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                volume += (min(height[stack[-1]], height[i]) - height[top]) * distance
                
            stack.append(i)
        
        return volume
                
            
            
                