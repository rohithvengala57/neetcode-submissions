from queue import PriorityQueue
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = PriorityQueue()
        m = 10**9
        for x1, x2 in points:
            q.put((math.sqrt((x1)**2 + (x2)**2), (x1, x2)))
            m = min(m,math.sqrt((x1)**2 + (x2)**2))
        ans = []
        for i in range(k):
            if not q.empty():
                ans.append(q.get()[1])
        return ans