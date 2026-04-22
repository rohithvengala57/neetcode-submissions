class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for i in adjList[node]:
                if i != prev:
                    if not dfs(i, node): return False
            return True
        return dfs(0, -1) and len(visit) == n