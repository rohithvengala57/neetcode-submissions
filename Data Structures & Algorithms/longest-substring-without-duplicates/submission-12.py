class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        length  = 0
        start = 0
        if s:
            length+=1
            maxlength+=1
            visit = defaultdict(lambda: -1)
            visit[s[0]] = 0
            for i in range(1, len(s)):
                if visit[s[i]] < start:
                    length += 1
                    visit[s[i]] = i
                else:
                    start = visit[s[i]]
                    length = i - visit[s[i]]
                    visit[s[i]] = i
                maxlength = max(length, maxlength)
        return maxlength