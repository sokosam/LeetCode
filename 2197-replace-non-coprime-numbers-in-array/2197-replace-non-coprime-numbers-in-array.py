class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        

        def getGCD(a,b):

            maxNum = max(a,b)
            minNum = min(a,b)
            while maxNum % minNum != 0:
                new = maxNum % minNum
                maxNum = minNum
                minNum = new
            return minNum
        
        s = []
        for i in range(len(nums)):
            if len(s) == 0:
                s.append(nums[i])
            elif len(s) > 0:
                curr = nums[i]
                while len(s) > 0 and getGCD(curr, s[-1]) > 1:
                    a = s.pop()
                    b = curr
                    LCM = a*b//getGCD(b, a)
                    curr = LCM

                s.append(curr)
        return s

