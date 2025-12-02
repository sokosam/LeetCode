class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """
        any trapazoid only really depends on the top two points or the bottom two points


        Count of trapezoids formed for a single point= (num of points to the left and same level)
        and the # of (pairs of points in same level) for all levels 


        1  2 3 4 5 

        1*(num below) + 2*(num below) + 3(num below)
        (n(n - 1)//2)*(num below)

        2*(3*(3-1)//2) + 2*(2*(2-1)//2)
         
        """

        MOD = 10**9 +7

        running_points =0
        total = 0

        levels = defaultdict(int)

        for x,y in points:
            levels[y] +=1

        unique_levels = [key for key in levels]
        unique_levels.sort()

        for level in levels:

            points = levels[level]
            top_level = points*(points-1)//2
            total += top_level*running_points % MOD
            running_points += top_level
        return total %MOD


