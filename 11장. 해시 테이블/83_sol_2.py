# 169. Majority Element
# https://leetcode.com/problems/majority-element/

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

from typing import List
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dict 사용하여 이미 체크 한 것은 지나가자
        counts = collections.defaultdict(int)

        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            
            if counts[num] > len(nums) // 2:
                return num