class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        
        ans = [0]*5
        ans[0] = (m-1)*(n-1)
        map = defaultdict(int)


        def isInside(x,y):
            nonlocal m,n
            return 0 <= x < (m-1) and 0<=y < (n-1)

        dirs = [(0,0), (-1,0) , (-1,-1), (0,-1)]
        for x,y in coordinates:
            for dx,dy in dirs:
                if isInside(x+dx, y + dy):
                    ans[map[(x+dx, y+dy)]] -=1
                    map[(x+dx, y+dy)] +=1
                    ans[map[(x+dx, y+dy)]] +=1
        return ans



            