# 561. Array Partition I
# https://leetcode.com/problems/array-partition-i/

# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) 
# such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        sum = 0
        pair = []
        
        for i in nums:
            pair.append(i)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
            
        return sum