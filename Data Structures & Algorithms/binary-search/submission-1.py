class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        print(mid)
        if nums[mid] == target:
            return mid
        if 0 < mid < len(nums): 
            a = self.search(nums[:mid], target)
            if a != -1:
                return a
        if 0 < mid < len(nums): 
            b = self.search(nums[mid:], target)
            if b != -1:
                return mid + b
        return -1