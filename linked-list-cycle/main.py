from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        items = set()
        while head and head.next:
            if head in items:
                return True
            items.add(head)
            head = head.next
        return False
