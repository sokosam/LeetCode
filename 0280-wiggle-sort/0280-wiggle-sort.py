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

        reverse = nums[:]
        reverse.sort(reverse = True)

        ordered = nums[:]
        ordered.sort()

        index = 0

        for i in range(len(nums)):
            if i % 2 == 1:
                nums[i] = reverse[i//2]
            else:
                nums[i] = ordered[i//2]
