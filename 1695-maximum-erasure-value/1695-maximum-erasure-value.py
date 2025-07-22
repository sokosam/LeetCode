class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        m = {}

        best = 0
        curr = 0
        prefix = [0]*(len(nums) + 1)
        breakpt = 0

        for index, i in enumerate(nums):
            prefix[index + 1] = prefix[index]  + i
            if i not in m:
                m[i] = index
                curr += i
            else:
                best = max(best,curr)
                # print(best,curr)
                curr = prefix[index + 1] - prefix[max(m[i],breakpt) + 1] 
                # print(prefix)
                # print(index + 1, m[i] + 1, curr, best )
                breakpt = max(breakpt, m[i])

                m[i] = index
        return max(best,curr)
