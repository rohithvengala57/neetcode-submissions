class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = defaultdict(list)
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
        visited = [0]
        que = deque()
        que.append(0)
        while que:
            for i in range(len(que)):
                node = que.popleft()
                for i in tree[node]:
                    if i in visited:
                        return False
                    visited.append(i)
                    que.append(i)
                    tree[i].remove(node)   
        print(visited)
        if len(visited) == n:
            return True
        else:
            return False

        # O-1,2,3  1-4  2-0  3-0
                    