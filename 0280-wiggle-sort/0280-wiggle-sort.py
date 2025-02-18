class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        """
        0 <= 1
        1 >= 2 
            1 >= 0, 2
        2 <= 3
        3 >= 4
            3 >= 2, 4
        4 <= 5
            5 >= 4, 6

        3 5 2 1 6 4
        1 3 2 4 5 6
        1 2 3 4 5 6
        1 6 3 5 2 4

        6 6 5 6 3 8
        3 5 6 6 6 8

        3 8 5 6 6 6


        1 2 3 4 5 6 7 8 9 10

        1 10 3 9 5 8 7 6 4 2
        1 10 3 9 5 8 7 4 6 2
        """

        for i in range(len(nums) - 1):
            if i % 2 == 0:
                temp = nums[i]
                nums[i] = min(temp, nums[i + 1])
                nums[i + 1] = max(temp, nums[i + 1])
            else:
                prev = nums[i - 1]
                next = nums[i + 1]

                if prev > nums[i]:
                    nums[i - 1], nums[i ] = nums[i], nums[i -1]
                if next > nums[i]:
                    nums[i + 1], nums[i] = nums[i] , nums[i + 1]
                    
        

