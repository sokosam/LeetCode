class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        if sum(nums) == 0: return 0

        def check(nums, queries):
            pref = [0]* (len(nums) + 1)

            for query in queries:
                start = query[0]
                end = query[1] + 1
                val = query[2]
                pref[start] -= val
                pref[end] += val

            curr = 0
            for i in range(len(nums)):

                curr += pref[i]
                if nums[i] + curr > 0:
                    return False
            return True

        ans = -1

        l = 0
        r = len(queries) - 1

        while l <= r:
            m = l + (r-l)//2


            veri = check(nums, queries[0:m + 1 ])

            if veri:
                ans = min(ans,m + 1 ) if ans != -1 else m + 1 
                r = m -1
            else:
                l = m + 1
        return ans