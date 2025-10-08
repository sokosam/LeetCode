class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        11223
          lrc
        
        111223

        1111111223
        lr     c
        1122
         lr     c
        """


        l = 0
        r= 1

        total = len(nums)

        for c in range(r + 1, len(nums)):
            if nums[l] != nums[c] or nums[r] != nums[c]:
                nums[r + 1] = nums[c]
                l +=1
                r +=1
            else:
                total -=1
        return total
