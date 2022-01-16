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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        rev = None
        slow = fast = head
        
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            # fast는 두칸씩이동
            fast = fast.next.next
            # rev에 slow 할당, rev.next에는 기존 rev할당하여 역순 만들기, slow 한칸 전진
            rev, rev.next, slow = slow, rev, slow.next
        
        # 홀수일때 한칸더 전진
        if fast:
            slow = slow.next
        
        # 팰린드 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        
        return not rev
        
