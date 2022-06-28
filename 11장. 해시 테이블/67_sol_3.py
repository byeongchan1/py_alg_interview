# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

from typing import List, Set
import bisect

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        # 둘다 정렬
        nums1.sort()
        nums2.sort()
        i = j = 0

        # 투 포인트 사용
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
        
        return result