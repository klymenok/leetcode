from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        loop = 0
        while a is not b:
            if a == headB:
                loop += 1
                if loop > 1:
                    return
            a = a.next if a.next else headB
            b = b.next if b.next else headA
        return a
