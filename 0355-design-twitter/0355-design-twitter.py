class Twitter:

    def __init__(self):
        self.time = 0

        self.feed = defaultdict(list)

        self.following = defaultdict(set)

        self.selfPosts = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        
        heapq.heappush(self.selfPosts[userId], [self.time, tweetId])
        if len(self.selfPosts[userId]) > 10:
            heapq.heappop(self.selfPosts[userId])
        
        self.time += 1
        return 

    def getNewsFeed(self, userId: int) -> List[int]:

        temp = []
        for user in self.following[userId]:
            arr = [ [-i[0],i[1]] for i in self.selfPosts[user].copy()]
            temp += arr
        temp += [ [-i[0],i[1]] for i in self.selfPosts[userId].copy()]

        heapq.heapify(temp)

        ans = []
        for i in range(10):
            if len(temp) > 0:
                curr = heapq.heappop(temp)
                ans.append(curr[1])
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        return
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        return
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)