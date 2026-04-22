class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from queue import PriorityQueue
        pqueue = PriorityQueue()
        ans = []
        nums = [-i for i in nums]
        for i in range(k):
            pqueue.put((nums[i], i))
        i=1
        first, index = pqueue.get()
        ans.append(first)
        if index >= i:
            pqueue.put((first, index))
        visit = [0]*len(nums)
        for j in range(k, len(nums)):
            pqueue.put((nums[j], j))
            val, track = pqueue.get()
            while track < i:
                val, track = pqueue.get()
                print(j, val, track)
            ans.append(val)
            i+=1
            if track >= i:
                pqueue.put((val, track))
        return [-i for i in ans]