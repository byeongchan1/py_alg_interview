# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, 
# and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        