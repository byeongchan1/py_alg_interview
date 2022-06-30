# 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 예외처리
        if not matrix:
            return False

        # 첫행 맨오른쪽 기준으로 판단
        row = 0
        col = len(matrix[0]) - 1
        
        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        
        return False