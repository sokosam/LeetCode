class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        ans= 0
        if len(nums) < 3:
            return 0
        diff = nums[1] - nums[0]
        total = 2
        for end in range(2, len(nums)):
            newDiff = nums[end] - nums[end -1 ]
            if newDiff != diff:
                if total >= 3:
                    ans += (total)*(total + 1)//2 - (2*total -1 )
                diff = newDiff
                total = 2
            else:
                total += 1
        
        if total >= 3:
            ans += (total)*(total + 1)//2 - (2*total -1 )     
        return ans