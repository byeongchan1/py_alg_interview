# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 연결리스트 뒤집기
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next        
        return prev

    # 연결리스트를 파이썬 리스트로 변환    
    def tolist(self, node: Optional[ListNode]) -> list:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    # 파이썬 리스트를 연결리스트로 변환
    def toReversedLinkedList(self, result:str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return prev
    
    # 두 연결 리스트의 덧셈    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.tolist(self.reverse(l1))
        b = self.tolist(self.reverse(l2))
        
        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))
        
        return self.toReversedLinkedList(str(resultStr))
                
            