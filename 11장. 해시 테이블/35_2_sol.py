# 77. Combinations
# https://leetcode.com/problems/combinations/

# Given two integers n and k, 
# return all possible combinations of k numbers out of the range [1, n].

# You may return the answer in any order.

import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))