class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        
        

        " 1 17 5 15 5 16 8"
        " + -  + -  +  - "

        "16, -12, 5, -5, 11, -8"

        """


        """
        prev1 = -1
        prev2 = -1
        i = 0
        ans = 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i -1]:
                i+=1
                continue
            if prev1 == -1:
                prev1 = nums[i]
                ans +=1
            elif prev2 == -1:
                print(nums[i], prev1)
                prev2 = nums[i]
                ans += 1
            elif nums[i] > prev2 > prev1 or prev1 > prev2 > nums[i]:
                prev2 = nums[i]
                i +=1
                continue
            else:
                prev1 = prev2
                prev2 = nums[i]
                ans+=1
            i +=1
        return ans