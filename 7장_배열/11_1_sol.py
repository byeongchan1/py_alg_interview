# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        p = 1
        
        # 왼쪽 곱셈 계산
        for i in range(len(nums)):
            results.append(p)
            p *= nums[i]
        
        # 오른쪽 곱셈 계산
        p = 1            
        for i in range(len(nums)-1, 0 - 1, -1):
            
            results[i] *= p
            p *= nums[i]
        
        return results
                
            
            