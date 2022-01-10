# 1. Two Sum
# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # target - 첫번째 수 = 두번째수
        # 두번째수를 빠르게 조회 가능하면 속도를 올릴 수있다.
        # dict 조회는 평균적으로 O(1)이다. (최악의 경우 O(n))
        
        # dict 조회를 위해 dict 만들기
        nums_map = {}
        
        # 키와 값을 바꾸어서 딕션어리 만들기
        for i, num in enumerate(nums):
            nums_map[num] = i
            
        # dict에 있다 판단은 key로 판단됨
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]