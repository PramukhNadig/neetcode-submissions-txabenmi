class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        rank = [1] * (n)
        par = [i for i in range(n)]

        def find(p):
            while p != par[p]:
                p = par[par[p]]
            return p
        
        def unite(p, q):
            a, b = find(p), find(q)
            if a == b:
                return False
            if rank[a] < rank[b]:
                a, b = b, a
            rank[a] += rank[b]
            par[b] = a
            return True
        
        for x, y in edges:
            if not unite(x, y):
                return False
        pars = []
        for x in range(n):
            pars.append(find(x))
        return len(set(pars)) == 1
        