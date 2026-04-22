class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxVolume = 0
        while l<r:
            maxVolume = max(min(heights[l], heights[r])*(r-l), maxVolume)
            if heights[l]>=heights[r]:
                r-=1
            else:
                l+=1
        return maxVolume