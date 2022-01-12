# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# Given the head of a singly linked list, return true if it is a palindrome.


import collections
from typing import Deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # 자료형 데크 선언
        list_ : Deque = collections.deque()

        if not head:
            return True

        # node는 head에서 호출 한 값 넣음
        node = head
        
        while node is not None:
            list_.append(node.val)
            node = node.next
        
        
        while len(list_) > 1:
            if list_.pop() != list_.popleft():
                return False
                    
        return True