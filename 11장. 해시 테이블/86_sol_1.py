# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(i, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)