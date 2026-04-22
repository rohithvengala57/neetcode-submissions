class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for course, pre in prerequisites:
            courseMap[course].append(pre)
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            pre = courseMap[course]
            visit.add(course)
            for i in pre:
                if not dfs(i): return False
            visit.remove(course)
            courseMap[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

                