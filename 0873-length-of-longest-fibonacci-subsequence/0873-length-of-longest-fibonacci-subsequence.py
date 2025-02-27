class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """

        1 2 3 4  5  6  7  8
        1 3 6 10 15 21 28 36



        """

        # dp = [[False for _ in range(len(arr))] for _ in range(len(arr))]
        # exists = set()

        # for i in range(len(arr)):
        #     exists.add(arr[i])
        #     for j in range(i +1, len(arr)):
        #         if arr[i] + arr[j] < arr[-1]:
        #             exists.add(arr[i] + arr[j])
        #             if dp[arr[i]][arr[j]] == 0:
        #                 dp[arr[i]][arr[j]] = True
        
        # print(dp)

        

        dp = {}

        for i in range(len(arr)):
            for j in range(i +1, len(arr)):
                # if i <j//2
                val =arr[i] + arr[j]

                if val > arr[-1]: continue
                adj = (arr[j])
                if val in dp:
                    dp[val].add(adj)
                else:
                    dp[val] = {adj}
        # print(dp)

        def check(v1, v2):
            prev = v2 -v1
            print(prev, v2, v1)
            if prev not in dp:
                if v1 in dp:
                    return 4
                else:
                    return 3
            return check(prev, v1) + 1
        
        best = 0
        for i in range(len(arr) -1, -1 ,-1):
            val = arr[i]
            if val not in dp:
                continue
            for k in dp[val]:
                best = max(check(k, val), best) 
            if best < 3:
                best = 0
            
        # def moveDown(val):
        return best
        # 8 
        # 8 -5 = 3  1
        # 5 - 3 = 2 2
        # 3 -2 = 1 5