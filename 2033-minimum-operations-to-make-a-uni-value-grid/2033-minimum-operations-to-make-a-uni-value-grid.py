class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        z =[]
        for row in grid:
            for col in row:
                z.append(col)
        
        z.sort()
        val = z[len(z)//2]
        
        amount = 0
        for row in grid:
            for col in row:

                if abs(val - col) % x!= 0:
                    return -1
                amount += abs(val-col)//x
        
        return amount