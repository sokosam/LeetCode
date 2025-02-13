class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        pref = [0]* (len(nums) + 1)

        for query in queries:
            start = query[0]
            end = query[1] + 1

            pref[start] -=1
            pref[end] += 1

        curr = 0
        for i in range(len(nums)):

            curr += pref[i]
            if nums[i] + curr > 0:
                return False
        return True