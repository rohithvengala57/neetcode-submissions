class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        visit = set()
        def dfs(node, ):
            if node not in visit:
                visit.add(node)
                for i in adjList[node]:
                    dfs(i)
        ans = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                ans+=1
        return ans