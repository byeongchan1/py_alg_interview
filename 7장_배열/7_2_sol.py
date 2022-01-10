# 1. Two Sum
# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i, n in enumerate(nums):
            complement = target - n
            # n 빼고나서 complement 있는지 확인하기
            
            # list에 index method 사용
            if complement in nums[i + 1:]:
                return [i, nums[i+1:].index(complement) + (i + 1)]
            
            # 1번풀이와 같이 O(n^2) 이지만, 속도가 더 빠르다.
            