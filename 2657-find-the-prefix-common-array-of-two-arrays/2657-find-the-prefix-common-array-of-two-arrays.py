class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        ans = []
        found = 0
        for i in range(len(A)):

            val1 = abs(A[i]) -1
            val2 = abs(B[i]) -1

            if A[val2] < 0:
                found +=1
            A[val2] *= -1
            if A[val1] < 0:
                found +=1
            A[val1] *= -1

            ans.append(found)
        return ans









