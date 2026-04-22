class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict
        if len(t) > len(s): return ""
        scount = defaultdict(int)
        tcount = Counter(t)
        start = 0
        have = 0
        need = len(tcount)
        ans = []
        minlen = 10**9
        for i in range(len(s)):
            scount[s[i]]+=1
            if scount[s[i]] == tcount[s[i]]:
                have+=1
            while need == have:
                if minlen > i-start+1:
                    ans.append((start, i))
                    minlen = i-start + 1
                scount[s[start]] -= 1
                if scount[s[start]] < tcount[s[start]]:
                    have-=1
                start += 1


        if ans:
            return s[ans[-1][0]: ans[-1][1]+1]
        else:
            return ""
#"ADOBECODEBANC"
#"ABC"