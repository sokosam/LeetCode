class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.m = {}

        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.m[tokenId] = currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.m:
            if currentTime < self.m[tokenId] + self.timeToLive:
                self.m[tokenId] = currentTime
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        val = 0
        deleted = []
        for i in self.m:
            if self.m[i] + self.timeToLive > currentTime:
                val +=1
            else:
                deleted.append(i)
        for i in deleted:
            del self.m[i]
        return val

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)