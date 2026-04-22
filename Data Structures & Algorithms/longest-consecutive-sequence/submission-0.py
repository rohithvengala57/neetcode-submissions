class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLength = 0
        for i in nums:
            length = 0
            if i - 1 not in nums:
                while i + length in nums:
                    length += 1
                maxLength = max(length, maxLength)
        return maxLength