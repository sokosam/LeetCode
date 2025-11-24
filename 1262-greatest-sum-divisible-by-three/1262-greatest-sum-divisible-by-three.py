class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        

        nums.sort(reverse = True)

        m = {1 : [] , 2 : []}

        # m = defaultdict(int)
        ans = 0

        for i in nums:
            if i %3 == 0:
                ans +=i
            else:
                heappush(m[i%3], i)
        
        ones = len(m[1])
        twoes = len(m[2])*2

        both = ones + twoes
        if both % 3 == 0:
            return ans + sum(m[1]) + sum(m[2])
        elif both % 3 == 1:
            best = 0
            if len(m[1]) > 0:
                best = ans + sum(m[1]) + sum(m[2]) - min(m[1])

            if len(m[2]) >= 2:
                heappop(m[2])
                heappop(m[2])
                best = max(best, sum(m[1]) + sum(m[2]) + ans)
            return best
        else:
            best = 0
            if len(m[2]) > 0:
                best = ans + sum(m[1]) + sum(m[2]) - min(m[2])
            if len(m[1]) >= 2:
                heappop(m[1])
                heappop(m[1])
                best = max(best, sum(m[1]) + sum(m[2]) + ans)
            return best