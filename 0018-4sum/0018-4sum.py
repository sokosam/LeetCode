class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        -2, -1 ,0 ,0 ,1 ,2

        """
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            val1 = nums[i]
            for j in range(i + 1, len(nums)):
                val2 = nums[j]
                currTarget = target - val1 - val2
                l = j + 1
                r = len(nums) - 1

                while l < r:
                    if nums[r] + nums[l] == currTarget:
                        ans.add((val1,val2, nums[l], nums[r]))
                        r -=1
                        l +=1
                    elif nums[r] + nums[l] < currTarget:
                        l += 1
                    else:
                        r -= 1
        return list(ans)

