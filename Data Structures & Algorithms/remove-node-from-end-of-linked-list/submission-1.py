# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        main = head
        prev = None
        target = None
        while head:
            if n == 1:
                target = main
            elif n < 1:
                prev = target
                target = target.next
            head = head.next
            n-=1
        if prev:
            prev.next = target.next if target else None
        else:
            main = main.next
        return main