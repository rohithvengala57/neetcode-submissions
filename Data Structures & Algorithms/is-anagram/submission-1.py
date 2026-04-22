class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted([i for i in s]) == sorted([i for i in t])