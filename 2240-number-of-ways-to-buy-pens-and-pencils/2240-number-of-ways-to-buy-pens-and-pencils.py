class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:

        i = 0
        ways = 0


        while i*cost1 <= total:
            left_over = total - i*cost1
            curr_ways = left_over//cost2 + 1
            # print(curr_ways, left_over, i)
            ways += curr_ways  
            i+=1
        return ways
