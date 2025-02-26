class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        
        

        " 1 17 5 15 5 16 8"
        " + -  + -  +  - "

        "16, -12, 5, -5, 11, -8"

        """


        """
        ans = []
        i = 0
        while i < len(nums):
            if i == 0:
                ans.append(nums[i])
                i += 1
                continue
            while i < len(nums) and nums[i] == ans[-1]:
                i += 1
            if i >= len(nums): break
            if len(ans) == 1:
                ans.append(nums[i])
            elif (nums[i] > ans[-1] > ans[-2]) or (ans[-2] > ans[-1] > nums[i]):
                ans.pop()
                ans.append(nums[i])
            else:
                ans.append(nums[i])
            i+=1

        return len(ans)