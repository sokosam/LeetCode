class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        """
        height is irrelevant

        greedy seems to work

        """

        points.sort()
        total = 0
        for i in range(len(points)):
            if i == 0:
                farthest = points[i][0] + w
                total += 1
                continue
            x = points[i][0]
            if x > farthest:
                farthest = x + w
                total +=1
        return total
            

