# 77. Combinations
# https://leetcode.com/problems/combinations/

# Given two integers n and k, 
# return all possible combinations of k numbers out of the range [1, n].

# You may return the answer in any order.

# 이해가 잘 안됩니다
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results