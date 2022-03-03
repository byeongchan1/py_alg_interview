# 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        return (root.val if L <= root.val <= R else 0) + \
               self.rangeSumBST(root.left, L, R) + \
               self.rangeSumBST(root.right, L, R)