from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l = 1
        _head = head
        while head.next:
            head = head.next
            l += 1
        head.next = _head
        for _ in range(1, l - k % l):
            _head = _head.next
        head = _head.next
        _head.next = None
        return head
