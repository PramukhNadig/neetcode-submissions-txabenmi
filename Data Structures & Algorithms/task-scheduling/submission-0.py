class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = 0
        if n == 0:
            return len(tasks)
        c = Counter(tasks)
        task = [(-v, k) for (k, v) in c.items()]
        readd = deque()
        heapq.heapify(task)
        

        while task or readd:
            print(t, task, readd)
                # print('fgdsnjo')
            if readd:
                ramt, rcurr, time = readd[0]
                if time == t:
                    readd.popleft()
                    heapq.heappush(task, (ramt, rcurr))
            if task:
                amt, curr = heapq.heappop(task)
                amt *= -1
                # print((amt, curr))
                amt -= 1
                if amt > 0:
                    readd.append((-amt, curr, t + n + 1))
                t += 1
            else:
                if readd:
                    t = readd[0][2]
        return t

            