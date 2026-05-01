class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        if groupSize == 1:
            return True
        def remove(low):
            for i in range(groupSize):
                if not c[low + i]:
                    return False
                c[low + i] -= 1
            return True
        for num in range(max(hand)):
            while c[num]:
                if not remove(num):
                    return False
        # print(c.values())
        return True if sum(c.values()) == 0 else False