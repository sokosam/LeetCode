class Solution:
    def reorganizeString(self, s: str) -> str:
        

        x = [[0,chr(i + ord('a'))] for i in range(26)]

        for i in s:
            x[ord(i) - ord('a')][0] +=1
        
        y = [(-x[i][0], x[i][1]) for i in range(len(x))]
        heapq.heapify(y)

        ans = ""
        prev = None
        while y and y[0][0] != 0:
            curr  = heapq.heappop(y)
            ans += curr[1]
            if prev and prev[0] != 0:
                heapq.heappush(y,prev)
            prev = (curr[0] + 1, curr[1])
        if prev and prev[0] != 0:
            return ""
        return ans