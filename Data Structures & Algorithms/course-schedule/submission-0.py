class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for x, y in prerequisites:
            adj[y].append(x)
        exp = set()
        def dfs(x, vis):
            if x in exp:
                return True
            if x in vis:
                return False
            vis.add(x)
            for nei in adj[x]:
                if nei in vis:
                    return False
                if not dfs(nei, vis):
                    return False
            exp.add(x)
            vis.remove(x)
            return True        
        for n in range(numCourses):
            if not dfs(n, set()):
                return False
        return len(exp) == numCourses
