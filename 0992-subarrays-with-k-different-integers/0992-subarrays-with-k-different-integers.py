class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """


        nums = [1,2,1,3,1,2,1]
        prefix = [1,2,2,3,3,3,3]
        prefix = [1,2,2,3,3,3,3]

        prefix = [1,2,2,2,3] 
                  0 1 2 3

                  n(n+1)//2 - (k - 1)(k)//2

        prefixFromRight = [1,2,3,3,3]


                

        uniqueOnRight = [3,3,2,1,0]

        uniqueOnLeft =  [0,1,2,3,3]

        once we have some subarray that has a k unique numbers, the only way for that subarray to extend is to reuse the unique numbers

        2 
        """


        # def distinctK(nums, k, size):
            

        #     m = {}
        #     distinct = 0
        #     arrays = 0

        #     for i in range(len(nums)):
        #         if nums[i] not in m:
        #             m[nums[i]] = 1
        #         else:
        #             m[nums[i]] += 1
            
        #         if m[nums[i]] == 1:
        #             distinct +=1

                
        #         if i >= size:
        #             m[nums[i- size]] -= 1
        #             if m[nums[i-size]] == 0:
        #                 distinct -=1
                
        #         if distinct == k and i >= size - 1:
        #             arrays +=1
        #     return arrays

        # ans = 0
        # for i in range(k, len(nums) + 1):
        #     ans += distinctK(nums, k , i)
        # return ans


        def subArraysAtmostK(nums, k):
            distinct = 0
            m = {}
            total = 0
            start = 0

            for end in range(len(nums)):
                number = nums[end]
                if number in m:
                    m[number] += 1
                else:
                    m[number] = 1      
                distinct += 1 if m[number] == 1 else 0

                while start <= end and distinct > k:
                    new_number = nums[start]
                    m[new_number] -=1
                    if m[new_number] == 0:
                        distinct -= 1
                    start +=1
                
                total += end - start + 1
            return total
        return subArraysAtmostK(nums, k) - subArraysAtmostK(nums, k -1)

