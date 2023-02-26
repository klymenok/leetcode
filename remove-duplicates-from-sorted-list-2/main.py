from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        new_pointer = None
        to_skip = None

        while head:
            if not new_head:
                if head.val != to_skip and ((head.next and head.val != head.next.val) or (not head.next)):
                    new_head = new_pointer = head
                else:
                    to_skip = head.val
            else:
                if head.val != to_skip and new_pointer.val != head.val and ((head.next and head.val != head.next.val) or (not head.next)):
                    new_pointer.next = head
                    new_pointer = head
                else:
                    to_skip = head.val
            head = head.next
        if new_pointer:
            new_pointer.next = None
        return new_head
