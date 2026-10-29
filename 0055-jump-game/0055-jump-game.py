class Solution:
    def canJump(self, nums: list[int]) -> bool:
        best_jump = 0
        for idx, i in enumerate(nums):
            if idx == 0:
                best_jump = i
                continue
            
            if idx > best_jump:
                return False

            best_jump = max(best_jump, idx + i)
        return True

