class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while i<=j:
            print(i,j)
            mid = (i+j)//2
            print(mid)
            if nums[mid] == target:
                return mid
            if nums[i] <= nums[mid]:
                if target > nums[mid] or target < nums[i]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                if target < nums[mid] or target > nums[j]:
                    j = mid - 1
                else:
                    i = mid + 1  
        return -1