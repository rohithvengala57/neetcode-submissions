class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append([equations[i][1], values[i]])
            graph[equations[i][1]].append([equations[i][0], 1/values[i]])
        def dfs(node,target):  
            if node not in graph or target not in graph:
                return -1
            if node == target:
                return 1
            for i,j in graph[node]:
                if not visited[i]:
                    visited[i] = 1
                    result = dfs(i,target)
                    if result != -1:
                        return j*result
            return -1
        ans = []
        for i,j in queries:
            visited = defaultdict(int)
            print(i==j)
            ans.append(dfs(i,j))
        return ans
