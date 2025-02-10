class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """


        candles: [0,0,1,1,1,2,2,2,2,3]
        plates:  [1,2,2,3,4,4,5,6,7,7]

                  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
        candles: [0,0,0,1,1,1,2,2,2,2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6]
        plates:  [1,2,3,3,4,5,5,6,7,8, 9,10,10,11,12,12,12,13,14,14,15]

        """

        candles = []
        plates = []
        currCandles = 0
        currPlates = 0
        candleMaps = {0 : [0, -1]}
        for i in range(len(s)):
            if s[i] == '*':
                currPlates +=1
            else:
                candleMaps[currCandles][1] = i
                currCandles += 1
                candleMaps[currCandles] = [i, -1]
            candles.append(currCandles)
            plates.append(currPlates)

        ans = []
        # print(candleMaps)
        for query in queries:
            left = query[0]
            right = query[1]
            leftCandle =candles[left]
            if leftCandle == 0 or candleMaps[leftCandle][0] < left:
                left = candleMaps[leftCandle][1]
                if left == -1 or left >= right:
                    ans.append(0)
                    continue
            
            right = candleMaps[candles[right]][0]
            # print(left,right)
            ans.append(plates[right] - plates[left])
        return ans
            


    