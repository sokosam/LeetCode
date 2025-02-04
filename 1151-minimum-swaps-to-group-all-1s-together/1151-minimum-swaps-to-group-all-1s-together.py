class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        size = sum(data)
        minSwap = size - sum(data[0:size])
        l, r = 0, size - 1

        current = sum(data[0:size])

        for i in range(r+1,len(data)):
            current -= data[l]
            l += 1
            current += data[i]
            minSwap =  min(minSwap, size - current)
        
        return minSwap


        
