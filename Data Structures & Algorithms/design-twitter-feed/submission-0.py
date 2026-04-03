import collections

class Twitter:

    def __init__(self):
        self.user_tweets = collections.defaultdict(collections.deque)
        self.following = collections.defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].appendleft((tweetId, self.timestamp))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:

        news_feed = []
        news_feed.extend(self.user_tweets[userId])

        for followee_id in self.following[userId]:
            news_feed.extend(self.user_tweets[followee_id])
        news_feed.sort(key=lambda x: x[1], reverse=True)
        return [tweet_id for tweet_id, timestamp in news_feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

