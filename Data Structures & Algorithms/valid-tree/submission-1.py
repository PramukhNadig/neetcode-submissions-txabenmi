class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        rank = [0] * (n)

        def find(n):
            p = par[n]
            while p != par[p]:
                p = par[p]
            return p
        
        def union(n, m):
            a, b = find(n-1), find(m-1)
            if a == b:
                return False
            if rank[a] < rank[b]:
                a, b = b, a
            rank[a] += rank[b]
            par[b] = a
            return True
        for n1, n2 in edges:
            if not union(n1, n2):
                return False
        
        count = 0
        for ind, val in enumerate(par):
            if ind == val:
                count += 1
        return count == 1