# 78. Subsets
# https://leetcode.com/problems/subsets/

# Given an integer array nums of unique elements, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

# 이해가 잘 안되어유
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            # 매 번 결과 추가
            result.append(path)

            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result