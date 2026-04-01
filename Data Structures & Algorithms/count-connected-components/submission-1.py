class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [0] * (n)
        count = 0
        def find(n):
            p = par[n]
            while p != par[p]:
                p = par[p]
            return p
        
        def union(n, m):
            a, b = find(n-1), find(m-1)
            if a == b:
                return
            if rank[a] < rank[b]:
                a, b = b, a
            rank[a] += rank[b]
            par[b] = a
        
        for n1, n2 in edges:
            union(n1, n2)
        
        for ind, val in enumerate(par):
            if ind == val:
                count += 1
        return count