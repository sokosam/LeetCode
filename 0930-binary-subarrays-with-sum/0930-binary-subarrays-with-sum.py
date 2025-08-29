class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        
        def subarrayAtMostGoal(nums, goal):
            current = 0
            total = 0
            start = 0


            for end in range(len(nums)):

                current += nums[end]

                while start <= end and current > goal:
                    current -= nums[start]
                    start +=1
                

                total += end - start + 1
            return total
        return subarrayAtMostGoal(nums, goal) - subarrayAtMostGoal(nums, goal- 1)





