class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        
        reds = 0
        whites = 0
        blues = 0
        for i in nums:
            if i == 0:
                reds +=1
            elif i == 1:
                whites += 1
            else:
                blues += 1
        
        curr = 0
        for i in range(reds):
            nums[curr] = 0
            curr +=1

        for i in range(whites):
            nums[curr] = 1
            curr +=1

        for i in range(blues):
            nums[curr] = 2
            curr += 1
        return nums 



