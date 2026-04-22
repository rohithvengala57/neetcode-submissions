class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = 10**9
        piles.sort()
        l = 1
        m = max(piles)
        while l<=m:
            mid = (l+m)//2
            hours = sum([math.ceil(i/mid) for i in piles])
            if hours <= h:
                ans = min(ans, mid)
                m = mid - 1
            else:
                l = mid + 1
        return ans
            