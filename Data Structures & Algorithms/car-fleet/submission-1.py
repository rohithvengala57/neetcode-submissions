class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        print(sorted(zip(position, speed))[::-1])
        for i in sorted(zip(position, speed))[::-1]:
            if stack:
                if (a:=(target - stack[-1][0]) / stack[-1][1]) < (b:=(target - i[0]) / i[1]):
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack)