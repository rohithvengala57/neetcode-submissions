# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t = head if head else None
        r = head.next if head and head.next else None
        while r:
            if t == r:
                return True
            t = t.next
            r = r.next
            if r:
                r=r.next
        return False