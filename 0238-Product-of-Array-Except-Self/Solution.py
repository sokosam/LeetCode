# Completed on: 9/15/2024
# Submission: https://leetcode.com/problems/product-of-array-except-self/submissions/1391596908/
# Time Complexity: O(n)
# Space Complexity: O(n) 

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        left = []
        right = []
        curr = 1
        for i in nums:
            curr *=i
            left.append(curr)
        
        i = len(nums) -1
        curr = 1
        while i >=0:
            curr *=nums[i]
            right.append(curr)
            i -=1
        right = list(reversed(right))        

        discluded = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0: 
                discluded[i] = right[1]
            elif i == len(nums) -1:
                discluded[i] = left[-2]
            else:
                discluded[i] = left[i- 1] * right[i +1]
        return discluded