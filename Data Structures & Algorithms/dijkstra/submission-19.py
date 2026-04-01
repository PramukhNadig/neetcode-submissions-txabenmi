class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        res = {}
        for i in range(n):
            adj[i] = []
        for s, d, w in edges:
            adj[s].append([d, w])
        
        print(adj)
        minHeap = [[0, src]]

        while len(minHeap) > 0:
            curDist, curNode = heapq.heappop(minHeap)
            if curNode in res:
                continue
            res[curNode] = curDist

            for newNode, newDist in adj[curNode]:
                if newNode not in res.keys():
                    heapq.heappush(minHeap, [curDist + newDist, newNode])
            
        for i in range(n):
            if i not in res:
                res[i] = -1
        return res
