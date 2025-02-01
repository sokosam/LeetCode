class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        l = 0
        r = sum(data)
        total = r


        countOnes = 0
        for i in range(r):
            countOnes+= data[i]
        ans = float('inf')
        ans = min(ans, total - countOnes)
        
        while r < len(data):
            
            if data[l] == 1:
                countOnes -= 1
            if data[r] ==1:
                countOnes +=1
            
            ans = min(ans, total - countOnes)
            l +=1
            r +=1
        return ans
            
