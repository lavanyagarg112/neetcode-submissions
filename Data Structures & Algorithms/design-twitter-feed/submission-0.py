class Twitter:

    def __init__(self):
        self.tweets = {} # track 10 per user
        self.following = {}
        self.allTweets = []
        self.RECENT_COUNT = 10
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = deque()
        
        if len(self.tweets[userId]) > self.RECENT_COUNT:
            self.tweets[userId].popleft()
        self.tweets[userId].append(tweetId)

        self.allTweets.append(tweetId)
        
    def getFollowerTweets(self, userId):
        following = [userId]
        if userId in self.following:
            following += self.following[userId]
        tweets = []
        for p in following:
            if p in self.tweets:
                tweets.extend(self.tweets[p])

        result = []
        count = 0
        for i in range(len(self.allTweets)-1, -1, -1):
            if count == self.RECENT_COUNT:
                break
            t = self.allTweets[i]
            if t in tweets:
                result.append(t)
                count += 1
        
        return result


    def getNewsFeed(self, userId: int) -> List[int]:
        return self.getFollowerTweets(userId)

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # assuming happy path
        self.following[followerId].remove(followeeId)
        
