class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i]+=1
        bucket = [[] for _ in range(len(nums))]
        for i,j in counts.items():
            bucket[j-1].append(i)
        ans = []
        print(bucket)
        for i in reversed(bucket):
            if i and k!=0:
                ans=ans+i
                k-=len(i)
        return ans