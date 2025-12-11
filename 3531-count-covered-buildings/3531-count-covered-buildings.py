class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        

        xdir = defaultdict(lambda : [float('inf'), float('-inf')])
        ydir = defaultdict(lambda : [float('inf'), float('-inf')])

        for building in buildings:
            x,y = building
            ydir[x] = [min(ydir[x][0], y), max(ydir[x][1], y)]
            xdir[y] = [min(xdir[y][0], x), max(xdir[y][1], x)]

        total = 0
        for building in buildings:
            
            x,y = building
            miny,maxy = ydir[x]
            minx, maxx = xdir[y]
            if x ==minx or x == maxx:
                continue
            if y == miny or y == maxy:
                continue
            total +=1
        return total
