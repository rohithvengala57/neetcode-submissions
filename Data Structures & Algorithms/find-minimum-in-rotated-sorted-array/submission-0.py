class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = 10**9
        i = 0
        j = len(nums)-1
        while i<=j:
            mid = (i+j)//2
            ans = min(nums[mid], ans)
            if nums[mid]>nums[j]:
                i = mid+1
            else:
                j = mid-1
        return ans