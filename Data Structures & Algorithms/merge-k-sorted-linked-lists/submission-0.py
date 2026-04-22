# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self,other): 
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from queue import PriorityQueue
        a = PriorityQueue()
        for i in lists:
            if i: a.put(i)
        ans = ListNode()
        node = ans
        while a.qsize()>0:
            node.next = a.get()
            node = node.next
            if node and node.next:
                a.put(node.next)
        return ans.next