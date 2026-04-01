class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        degrees = [0] * numCourses
        for x, y in prerequisites:

            adj[y].append(x)
        res = []
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
            vis.remove(x)
            exp.add(x)
            res.append(x)
            return True
        s = set()
        for i in range(numCourses):
            if not dfs(i, s):
                return []
        return res[::-1]