class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = 1
        for i in nums:
            output.append(prefix)
            prefix*=i
        prefix = 1
        for i in range(len(nums))[::-1]:
            output[i]*=prefix
            prefix*=nums[i]
        return output