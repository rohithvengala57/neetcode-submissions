class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = [0]*len(nums)
        rp = [0]*len(nums)
        lp[0] = nums[0]
        rp[-1] = nums[-1]
        for i in range(1,len(nums)):
            lp[i] = lp[i-1]*nums[i]
        for i in reversed(range(len(nums)-1)):
            rp[i] = rp[i+1]*nums[i]
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(rp[1])
            elif i == len(nums)-1:
                ans.append(lp[-2])
            else:
                ans.append(lp[i-1]*rp[i+1])
        print(lp,rp)
        return ans