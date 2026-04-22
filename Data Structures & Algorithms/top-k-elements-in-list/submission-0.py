class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i]+=1
        sortcounts = [(k,v) for k,v in sorted(counts.items(), key = lambda item: -item[1])]
        ans = []
        for i in range(k):
            ans.append(sortcounts[i][0])
        return ans