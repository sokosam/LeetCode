class Solution:
    def __init__(self):
        self.dp = {}
    def wordBreak(self, s: str, wordDict: List[str], curr = "" ) -> bool:
        if len(s) == 0: return True
        else:
            pter = 0
            while(pter < len(s)):
                if curr not in self.dp and s[0:pter +1] in wordDict:
                    if self.wordBreak( s[pter +1:], wordDict, curr + s[0:pter +1]):
                        return True
                pter+=1
            self.dp[curr] = True
            return False
        