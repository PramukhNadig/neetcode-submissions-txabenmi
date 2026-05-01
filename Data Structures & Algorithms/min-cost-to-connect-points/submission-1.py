class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        connections = []
        for first in range(len(points)):
            for second in range(first + 1, len(points)):
                x1, y1 = points[first]
                x2, y2 = points[second]
                dist = (abs(x2-x1)) + (abs(y2-y1))
                connections.append([dist, first, second])
        connections.sort()

        par = [i for i in range(len(points) + 1)]
        rank = [1] * (len(points) + 1)

        def find(p):
            while p != par[p]:
                p = par[par[p]]
            return p
        

        def unite(m, n):
            a, b = find(m), find(n)
            if rank[a] > rank[b]:
                a, b = b, a
            rank[b] += rank[a]
            par[a] = b
            return True
        res = 0
        for dist, x, y in connections:
            if find(x) != find(y):
                unite(x, y)
                res += dist
        return res
