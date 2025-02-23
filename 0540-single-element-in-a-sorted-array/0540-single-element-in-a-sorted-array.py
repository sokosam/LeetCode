class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r -l )//2

            left = nums[m - 1] if m -1 >= 0 else -1 
            right = nums[m + 1] if m + 1 < len(nums) else -1

            if left != nums[m] and right != nums[m]:
                return nums[m]

            print(m, r, l)
            if m -1 >= 0 and nums[m] == nums[m-1]:
                if (m-l + 1)% 2 == 1:
                    r = m - 2
                else:
                    l = m + 1
            
            elif m + 1 < len(nums) and nums[m] == nums[m+1]:
                if (r -m + 1)% 2 ==1:
                    l = m + 2
                else:
                    r = m - 1


        