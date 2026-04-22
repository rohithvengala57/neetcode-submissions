class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i, val in enumerate(temperatures):
            if stack:
                while stack and stack[-1][0] < val:
                    val1, j = stack.pop()
                    print(val1, j)
                    ans[j] = i - j
            stack.append((val, i))
        return ans