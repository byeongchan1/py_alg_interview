# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

# Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            # 부모 노드 부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root