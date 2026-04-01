class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        rank = [0] * n

        def find(n):
            p = par[n]
            while p != par[p]:
                p = par[par[p]]
            return p
        
        def union(m, n):
            a, b = find(m-1), find(n-1)
            if a == b:
                return False
            
            if rank[a] < rank[b]:
                a, b = b, a
            rank[a] += b
            par[b] = a
            return True
        
        for s, d in edges:
            if not union(s, d):
                return False
        
        count = 0
        for i, v in enumerate(par):
            if i == v:
                count += 1
        
        return count <= 1
