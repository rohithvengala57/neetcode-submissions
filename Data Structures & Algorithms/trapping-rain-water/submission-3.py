class Solution:
    def trap(self, height: List[int]) -> int:
        leftTrap = [0]*len(height)
        rightTrap = [0]*len(height)
        maxHeight = height[0]
        for i in range(1, len(height)-1):
            maxHeight = max(maxHeight, height[i])
            leftTrap[i] = maxHeight - height[i]
        maxHeight = height[-1]
        for i in reversed(range(1,len(height)-1)):
            maxHeight = max(maxHeight, height[i])
            rightTrap[i] = maxHeight - height[i]
        water = [min(i,j) for i,j in zip(leftTrap, rightTrap)]
        print(water)
        return sum(water)