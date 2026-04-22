class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        counts = [0]*26
        counter = [0]*26
        for i in range(len(s1)):
            counts[ord(s1[i])-97] += 1
            counter[ord(s2[i])-97] += 1
        match = 0
        for i in range(26):
            match += 1 if counts[i] == counter[i] else 0
        i = 0
        for j in range(len(s1), len(s2)):
            print(match, s2[i])
            if match == 26:return True
            if counts[ord(s2[i])-97] == counter[ord(s2[i])-97]:
                match -=1
            counter[ord(s2[i])-97] -= 1
            if counts[ord(s2[i])-97] == counter[ord(s2[i])-97]:
                match += 1
            i+=1
            if counts[ord(s2[j])-97] == counter[ord(s2[j])-97]:
                match -= 1
            counter[ord(s2[j])-97] += 1
            if counts[ord(s2[j])-97] == counter[ord(s2[j])-97]:
                match += 1
        return True if match == 26 else False
                
                