class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        """


            [-4, -4, 4] 

            [4, 6, 14]

            [0, 2, 10]

        """
        size = len(strategy)
        allPos = [0]*(size + 1)
        prefix_sum = [0]*(size + 1)
        
        r_sum = 0
        p_sum = 0

        for i in range(size):
            p_sum += abs(prices[i])
            allPos[i + 1] = p_sum

            r_sum += prices[i]*strategy[i]
            prefix_sum[i + 1] = r_sum


        # print(prefix_sum)
        # print(allPos)
        
        start = 0
        end = 0
        best = sum([prices[i]*strategy[i] for i in range(size)])

        while end < size + 1:
            
            if end - start == k  :
                total = prefix_sum[-1]
                total -= prefix_sum[end]
                total += prefix_sum[start]

                total +=allPos[end]
                total -= allPos[(end + start)//2]
                start += 1
                # print(total, start, end)
                best = max(best, total)
            end += 1
        return best
