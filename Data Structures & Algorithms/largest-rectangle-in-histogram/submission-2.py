class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        m = 0
        stack = []
        for i, val in enumerate(heights):
            start = i
            while stack and stack[-1][1] > val:
                a, b = stack.pop()
                m = max(m, b*(i-a))
                start = a
            stack.append((start, val))
        while stack:
            a, b = stack.pop()
            m = max((len(heights)-a)*b, m)
        return m

            