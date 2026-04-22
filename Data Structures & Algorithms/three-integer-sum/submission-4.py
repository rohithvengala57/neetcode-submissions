class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-1):
            x = i+1
            y = len(nums)-1
            while x<y:
                if nums[i]+nums[x]+nums[y]==0:
                    if [nums[i], nums[x], nums[y]] not in ans:
                        ans.append([nums[i], nums[x], nums[y]])
                    y-=1
                    x+=1
                elif nums[i]+nums[x]+nums[y]<0:
                    x+=1
                else:
                    y-=1
        return ans
