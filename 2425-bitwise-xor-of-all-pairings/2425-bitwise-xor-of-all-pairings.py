class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        count = {}
        ans = 0
        if len(nums2) % 2 == 1:
            for i in nums1:
                ans ^= i
        if len(nums1) % 2 == 1:
            for i in nums2:
                ans^= i
        return ans


        
        # ans = 0
        # for num in count:
        #     if count[num] % 2 == 1:
        #         ans ^= num
        # return ans
        # [2,1,3] [10,2,5,0] 
        # 2^10 2^2 2^5 2^0 1^10 1^2 1^5 1^0 3^10 3^2 3^5 3^0 
        #  1   3   4   5       6                7

        # [8,0,7,..... ]
        #   ^

        # (2^10) ^ 2 ^ 2
        # = 0

        # parity of the counts of numbers
        # if it is even it ends up adding a final sum zero
        # if it is odd then it is just x