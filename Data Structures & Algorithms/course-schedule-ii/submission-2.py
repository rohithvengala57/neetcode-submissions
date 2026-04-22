class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = collections.defaultdict(list)
        for course, pre in prerequisites:
            adjList[course].append(pre)
        ans = []
        visit = set()
        visited = set()
        def dfs(course):
            if course in visit:
                return False
            pre = adjList[course]
            visit.add(course)
            for i in pre:
                if not dfs(i): return False
            if course not in visited:
                ans.append(course)
            visited.add(course)
            visit.remove(course)
            adjList[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i): return []
        return ans