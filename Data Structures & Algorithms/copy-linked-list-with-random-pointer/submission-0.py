"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        main = head
        ans = Node(0)
        track = ans
        while main:
            track.next = Node(main.val)
            track = track.next
            track.random = main.random
            main.random = track
            main = main.next
        track = ans.next
        while track:
            if track.random:
                track.random = track.random.random
            else:
                track.random=None
            track=track.next
        return ans.next

        