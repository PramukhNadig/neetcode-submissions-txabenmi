class Twitter:

    def __init__(self):
        self.followerMap = defaultdict()
        self.tweets = defaultdict()
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        tmp = self.tweets.get(userId, [])
        heapq.heappush(tmp, [self.t, tweetId])
        self.tweets[userId] = tmp
        self.t += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.followerMap.get(userId, set())
        followers.add(userId)
        l = []
        for follower in followers:
            l += self.tweets.get(follower, [])
        l.sort()
        l.reverse()
        res = []
        for i in range(min(10, len(l))):
            res.append(l[i][1])
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followerMap.get(followerId, set()):
            tmp = self.followerMap.get(followerId, set())
            tmp.add(followeeId)
            self.followerMap[followerId] = tmp


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap.get(followerId, set()):
            tmp = self.followerMap.get(followerId, set())
            tmp.remove(followeeId)
            self.followerMap[followerId] = tmp

