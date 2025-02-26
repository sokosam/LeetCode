class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """

        1 -3 2 3 -4
        1 -2 0 3 -1


        2 -5 1 -4 3 -2
        2 -3 -2 -6 -3 -5


        """

        max1 = 0
        min1 = 0

        prefix = 0

        ans = 0

        for i in range(len(nums)):
            prefix += nums[i]
            print(prefix, max1,min1, ans)

            ans = max(ans,abs(prefix - max1) , abs(prefix -  min1))
            if i == 0:
                max1 =prefix
                min1 = prefix
            else:
                max1 = max(max1,prefix)
                min1 = min(min1,prefix)
        ans = max(abs(prefix), abs(min1), abs(max1), ans)
        return ans

