# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 예외처리
        if not head:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        # 반복하면서 노드 홀짝 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
            
        # 홀수 마지막에 짝수 헤드 연결
        odd.next = even_head
        
        return head