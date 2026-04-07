class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False, False, False]
        r1,r2,r3 = target
        for t1, t2, t3 in triplets:
            if t1 <= r1 and t2 <= r2 and t3 <= r3:
                res[0] = True if t1 == r1 else res[0]
                res[1] = True if t2 == r2 else res[1]
                res[2] = True if t3 == r3 else res[2]
        # print(res)
        return all(res)
            
