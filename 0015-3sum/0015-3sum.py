class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()


        for i in range(len(nums)):
            curr = nums[i]
            if curr > 0: break

            l = i + 1
            r = len(nums) - 1

            while l < r:
                s = nums[l]  + nums[r]
                if s + curr == 0:
                    ans.add((curr, nums[l], nums[r]))
                    l += 1
                    r -=1
                elif s + curr > 0:
                    r -= 1
                else:
                    l += 1
        return list(ans)
                