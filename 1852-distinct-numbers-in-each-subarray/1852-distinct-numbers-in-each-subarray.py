class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        

        m = {}

        l = 0 
        r = k

        countDistinct = 0

        for i in range(r):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1
            if m[nums[i]] == 1:
                countDistinct += 1
        
        ans = []
        ans.append(countDistinct)

        while r < len(nums):
            
            m[nums[l]] -= 1
            if m[nums[l]] == 0:
                countDistinct -= 1
            
            if nums[r] in m:
                m[nums[r]] +=1
            else:
                m[nums[r]] = 1
            if m[nums[r]] == 1:
                countDistinct +=1
            ans.append(countDistinct)
            l+=1
            r+=1
        return ans
            
