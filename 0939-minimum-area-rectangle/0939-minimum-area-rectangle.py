class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        """

        for any diagonal, check if 

        """

        cache = {}
        for point in points:
            if point[0] not in cache:
                cache[point[0]] = [point[1]]
            else:
                cache[point[0]].append(point[1])

        ans = float('inf')
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j: continue
                if points[i][1] < points[j][1] and points[i][0] < points[j][0]:
                    if points[j][1] not in cache[points[i][0]]:
                        continue
                    if points[i][1] not in cache[points[j][0]]:
                        continue
                    else:
                        ans = min(ans, (points[j][1] - points[i][1])* (points[j][0] - points[i][0]))
        
        return ans
