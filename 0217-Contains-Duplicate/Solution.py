# Completed on: 9/15/2024
# Submission: https://leetcode.com/problems/contains-duplicate/submissions/1391527817/
# Time Complexity: O(n)
# Space Complexity: O(k) 
#   k : Number of distinct elements
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen: return True
            else: seen.add(i)
        return False  
    
