class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        aSeen = set()
        pSeen = set()
        atlantic = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        pacific = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]


        q1 = deque()

        for i in range(len(heights)):
            q1.append((i, len(heights[0]) - 1 ))
            aSeen.add((i, len(heights[0]) - 1 ))
        
        for i in range(len(heights[0])):
            q1.append((len(heights) -1 , i))
            aSeen.add((len(heights) -1 , i))


        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        while q1:
            curr = q1.popleft()
            x,y = curr
            atlantic[x][y] = True

            for dx, dy in dirs:
                newX,newY = dx+x,dy+y
                if 0 <= newX < len(heights) and 0 <= newY < len(heights[0]):
                    if heights[x][y] <= heights[newX][newY] and (newX,newY) not in aSeen:
                        q1.append((newX,newY))
                        aSeen.add((newX,newY))


        q2 = deque()

        for i in range(len(heights)):
            q2.append((i, 0 ))
            pSeen.add((i, 0))
        
        for i in range(len(heights[0])):
            q2.append((0 , i))
            pSeen.add((0, i))


        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        while q2:
            curr = q2.popleft()
            x,y = curr
            pacific[x][y] = True

            for dx, dy in dirs:
                newX,newY = dx+x,dy+y
                if 0 <= newX < len(heights) and 0 <= newY < len(heights[0]):
                    if heights[x][y] <= heights[newX][newY] and (newX,newY) not in pSeen:
                        q2.append((newX,newY))
                        pSeen.add((newX,newY))

        ans = []
        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if pacific[x][y] and atlantic[x][y]:
                    ans.append([x,y])
        return ans
