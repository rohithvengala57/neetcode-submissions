from queue import PriorityQueue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        qstones = PriorityQueue()
        for i in stones:
            qstones.put(-i)
        while qstones.qsize() > 1:
            print(qstones.qsize())
            a = qstones.get()
            b = qstones.get()
            if a != b:
                qstones.put(-abs(a-b))
        if not qstones.empty():
            return -qstones.get()
        else:
            return 0