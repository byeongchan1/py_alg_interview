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
        
        # 예외처리
        if not head or (left == right):
            return head
        
        root = start = ListNode(None)
        root.next = head
        
        # start, end 지정
        for _ in range(left - 1):
            start = start.next
        end = start.next
        
        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            # 1 3 4 5
            start.next.next = tmp
            # 1 3 2 4 5
            
        return root.next