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
        # 함수를 이용하여 재귀로 해보자
        
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            # next에 node.next 백업
            # node.next에 prev 저장
            
            return reverse(next, node)
            # 다음 스텝은 node.next인 next, 저장 1번 한 prev인 node
            # 함수를 다음 스텝으로 호출함에 따라 재귀 형식 완성
        
        return reverse(head)