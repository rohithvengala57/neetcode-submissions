class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']
        i = 0
        while i<len(tokens):
            if tokens[i] not in op:
                stack.append(tokens[i])
            else:
                if stack:
                    a = stack.pop()
                    b = stack.pop()
                    print(b, a)
                    stack.append(str(int(eval(b+tokens[i]+a))))
            i+=1
        return int(float(stack[-1]))