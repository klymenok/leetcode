from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_next_unique(self, node: ListNode, value: int):
        while node.val == value:
            if not node.next:
                return None
            node = node.next
        return node

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = head
        while lst and lst.next:
            if lst.val == lst.next.val:
                lst.next = self.get_next_unique(lst, lst.val)
            lst = lst.next
        return head
