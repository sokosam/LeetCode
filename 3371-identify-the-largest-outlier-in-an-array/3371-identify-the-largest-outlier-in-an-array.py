class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        
        seen = {}

        summ = 0
        ans = float('-inf')
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] +=1 
            summ += i


        for i in seen:
            val = summ - i
            if val %2 == 1:
                continue
            
            if val//2 in seen:
                if val//2 == i:
                    if seen[val//2] > 1:
                        ans = max(ans,i)
                else:
                    ans = max(ans ,i )
        return ans
