class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        

        def oneDiff(s1, s2):
            if len(s1) != len(s2):
                return False
            
            found = False
            for i in range(len(s1)):
                if not found and s1[i] != s2[i]:
                    found = True
                elif s1[i] != s2[i] and found:
                    return False
            return True
        

        dp = [0]*len(words)

        arr = [[] for _ in range(len(words))]

        for i in range(len(words)):
            best = 1
            bestj = i
            for j in range(i, -1 ,-1):
                if groups[j] != groups[i] and oneDiff(words[i], words[j]):
                    if dp[j] + 1 > best:
                        bestj = j
                        best = dp[j] + 1
            dp[i] = best
            arr[i] = arr[bestj][:]
            arr[i].append(words[i])
        ans = []
        for i in range(len(arr)):
            if len(ans) < len(arr[i]):
                ans = arr[i]
        return ans
                

