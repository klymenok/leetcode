# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        _head = head
        while _head and _head.next:
            if _head.next.val == val:
                _head.next = _head.next.next
            else:
                _head = _head.next
        return head
