# 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)