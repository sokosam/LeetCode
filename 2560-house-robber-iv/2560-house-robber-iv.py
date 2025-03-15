class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        min_reward, max_reward = 1, max(nums)

        total = len(nums)
        while min_reward < max_reward:
            mid = min_reward + (max_reward - min_reward)//2
            possible = 0
            index =0
            while index < total:
                if nums[index] <= mid:
                    possible +=1
                    index += 2
                else:
                    index +=1
            
            if possible >= k:
                max_reward = mid
            else:
                min_reward = mid + 1
        return min_reward