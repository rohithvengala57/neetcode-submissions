class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            alphabets = [0 for i in range(26)]
            for j in i:
                alphabets[ord(j)-97]+=1
            ans[tuple(alphabets)].append(i)
        return ans.values()