class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0]*26
        ans = 0
        start = 0
        for i, val in enumerate(s):
            counts[ord(val)-65] += 1
            if (i-start+1) - max(counts) <= k:
                ans = max(ans, i-start+1)
            else:
                while (i-start+1) - max(counts) > k and start < len(s):
                    counts[ord(s[start])-65] -= 1
                    start += 1
        return ans
        