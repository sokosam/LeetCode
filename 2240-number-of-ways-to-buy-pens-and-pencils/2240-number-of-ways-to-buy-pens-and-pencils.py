class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        """
        
        c1 = 10 c2 = 5

        if c1 % c2 == 0
        ways_per_c1 = c1//c2

        and total % c1 == 0
        total_c1 = total//c1
        total_c1 , 0
        total_c1 - 1, ways_per_c1
        total_c1 - 2,  2*ways_per_c1
        ...
        0, total_c1*ways_per_c1

        == (total_c1)*(total_c1 +1)//2  + (total_c1)*(total_c1 +1)//2*ways_per_c1

        20, 10, 5
        total_c1 = 20//10 = 2
        ways_per_c1 =  2

        == 3 + 3*2
        == 9

        if total % c1 != 0:
            let total % c1 == 3
            r = 3
        == (total_c1)*(total_c1 +1)//2  + (total_c1)*(total_c1 +1)//2*(ways_per_c1+ 3)
        if c1 % c2 != 0:
            
        """

        i = 0
        ways = 0


        while i*cost1 <= total:
            left_over = total - i*cost1
            curr_ways = left_over//cost2 + 1
            # print(curr_ways, left_over, i)
            ways += curr_ways  
            i+=1
        return ways
