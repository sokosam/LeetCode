class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        start, summ, ans = 0,0, 0


        for end in range(len(nums)):
            summ += nums[end]

            if summ >= target:
                if ans == 0:
                    ans = end - start + 1
                else:
                    ans = min(ans, end - start +1)
            
            while summ >= target:
                if summ >= target:
                    ans = min(ans, end - start + 1)
                summ -= nums[start]

                start +=1

        return ans