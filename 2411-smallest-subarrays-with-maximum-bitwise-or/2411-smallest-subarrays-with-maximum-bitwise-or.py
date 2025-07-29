class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:


        def getBits(n):
            bitArr = []
            while n > 0:
                if n % 2 == 1:
                    bitArr.append(1)
                else:
                    bitArr.append(0)
                n//=2
            return bitArr

        globalArr=  {}
        ans = [-1]*len(nums)
        for i in range(len(nums) - 1, -1 ,-1):
            arr = getBits(nums[i])
            for index,l in enumerate(arr):
                if l == 1:
                    globalArr[index] = i
            
            worst = i
            for j in globalArr:
                worst = max(worst,globalArr[j])
            ans[i] = worst - i + 1
        return ans
        """

        6 110
        //2

        3 % 2 == 1 
        1 % 2 == 1
        0 % 2 == 0

        """
