class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for i in range(1, numRows):
            old = ans[-1]
            new = []
            for j in range(len(old) + 1):
                val = 0
                if j == 0 or j == len(old):
                    val = 1
                else:
                    val = old[j] + old[j - 1]
                new.append(val)
            ans.append(new)
        return ans

                
                
                    
