class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        

        def getDigitSum(x):
            
            x = str(x)
            ans =0
            for i in range(len(x) -1, -1, -1):

                ans += int(x[i])
            return ans
        

        m = {}

        ans = -1

        for i in range(len(nums)):
            digSum = getDigitSum(nums[i])

            if digSum not in m:
                m[digSum] = nums[i]
            else:
                ans = max(ans, nums[i] + m[digSum])
                m[digSum] = max(m[digSum], nums[i])
        return ans

