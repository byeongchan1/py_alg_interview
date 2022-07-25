# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxmize
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum