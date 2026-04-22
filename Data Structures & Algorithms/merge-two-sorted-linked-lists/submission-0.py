# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self,other): 
        return self.val < other.val


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        from queue import PriorityQueue
        a = PriorityQueue()
        if list1: a.put(list1)
        if list2: a.put(list2)
        ans = ListNode()
        node = ans
        while a.qsize()>0:
            node.next = a.get()
            node = node.next
            if node and node.next:
                a.put(node.next)
        return ans.next