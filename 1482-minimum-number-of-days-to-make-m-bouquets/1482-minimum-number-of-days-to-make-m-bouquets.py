class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """

        [10,10,10,10,10]

        [-1,7,7,12,12,12,-1]


        """

        if m*k > len(bloomDay):
            return -1

        
        l = 1
        r = max(bloomDay)
        ans = float('inf')

        def greedy(bloomDay,m,k,day):

            ans = 0
            end = 0
            start = 0

            while end < len(bloomDay):
                if bloomDay[end] > day:
                    start = end + 1
                    end = end + 1
                else:
                    if end - start + 1== k:
                        start = end + 1
                        end += 1
                        ans += 1
                    else:
                        end += 1
            return ans
        # print(greedy(bloomDay,m,k,2))
        while l <=r:
            days = l + (r-l)//2

            amount = greedy(bloomDay,m,k, days)

            if amount >= m:
                ans = min(ans, days)
                r = days - 1
            else:
                l = days + 1
        return ans


