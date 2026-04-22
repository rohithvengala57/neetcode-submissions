class Solution:
    from collections import defaultdict
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        edges = defaultdict(list)
        wordList.append(beginWord)
        for i in wordList:
            for j in range(len(i)):
                edges[i[:j]+'*'+i[j+1:]].append(i)
        ans = 1
        q = [beginWord]
        visit = set()
        visit.add(beginWord)
        while q:
            for i in range(len(q)):
                word = q.pop(0)
                if word == endWord:
                    return ans
                for j in range(len(word)):
                    for n_word in edges[word[:j]+'*'+word[j+1:]]:
                        if n_word not in visit:
                            visit.add(n_word)
                            q.append(n_word)
            ans+=1 
        return 0

