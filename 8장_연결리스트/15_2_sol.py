# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        
        while node:
            # node = [1,2,3]
            # prev = None
            
            next, node.next = node.next, prev
            # node.next는 next에 백업
            # 지금 node 부분 빼고 뒷부분 prev로 붙임

            # next = 2 3 None
            # node = 1 None

            prev, node = node, next
            # 원하던 prev는 현재 node + prev -> prev = node
            # node는 왼쪽 부분 빼고 저장 -> node = next

            
        return prev