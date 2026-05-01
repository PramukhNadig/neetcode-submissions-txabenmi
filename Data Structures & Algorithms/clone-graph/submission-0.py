"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodeDict = defaultdict()
        currToNode = defaultdict()
        q = [node]
        while q:
            curr = q.pop()
            if curr.val not in nodeDict.keys():
                n = Node(curr.val)
                nodeDict[curr.val] = n
                currToNode[curr] = n

            for nei in curr.neighbors:
                if nei.val not in nodeDict.keys():
                    q.append(nei)
        for no in currToNode.keys():
            for nei in no.neighbors:
                nodeDict[no.val].neighbors.append(currToNode[nei])
        return nodeDict[node.val]
                



