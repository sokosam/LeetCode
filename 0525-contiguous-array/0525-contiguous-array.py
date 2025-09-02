class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """


        0: 1 1 1 1 1 1 2 3 4
        1: 0 1 2 3 4 5 5 5 5


        """

        ratios = {}

        cnt0 = 0
        cnt1 = 0
        best = 0

        for index, i in enumerate(nums):
            cnt0 += i^1
            cnt1 += i^0

            ratio = cnt0 - cnt1
            if cnt0 == cnt1:
                best = max(best, cnt0*2)

            if ratio in ratios:
                best = max(best, index - ratios[ratio] )
            else:
                ratios[ratio] = index
        return best
