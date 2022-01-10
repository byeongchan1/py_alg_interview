# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        # two point 풀이
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        # 더 높은쪽을 향해 포인터 이동
        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            
            else:
                volume += right_max - height[right]
                right -= 1
            
        return volume
        
        

            
            
            
                