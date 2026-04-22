class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        return re.sub("[^0-9a-z]+", "", s.lower()) == re.sub("[^a-z]+", "", s.lower())[::-1]