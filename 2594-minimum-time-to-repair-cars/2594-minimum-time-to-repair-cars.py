class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 1
        r = min(ranks) * cars * cars
        best = float('inf')
        while l <=r:

            n = l + (r-l)//2
            done = 0
            for i in ranks:
                done += int(((n)//i)**(0.5))
            if done >= cars:
                best = min(best, n)
                r = n -1
            else:
                l = n + 1
        return best


            