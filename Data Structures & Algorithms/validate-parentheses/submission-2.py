class Solution:
    def isValid(self, s: str) -> bool:
        if s == "": return True
        check = {
            ')':'(',
            '}':'{' ,
            ']':'['
        }
        stack = [s[0]]
        i = 1
        while i < len(s):
            print(s[i])
            if (r:=check.get(s[i])) is not None:
                if not stack: return False
                val = stack.pop()
                print(val != r)
                if val != r:
                    return False
            else:
                stack.append(s[i])
            i+=1
        return False if stack else True
