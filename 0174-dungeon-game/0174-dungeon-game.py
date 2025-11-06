class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        worst = [[float('-inf') for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

        if dungeon[0][0] > 0:
            worst[0][0] = 0
        else:
            worst[0][0] = dungeon[0][0] -1

        def isWithin(dungeon, row,col):
            return row >= 0  and row < len(dungeon) and col >=0 and col < len(dungeon[0])

        dirs = [(-1,0), (0,-1)]
        for row in range(len(dungeon)):
            for col in range(len(dungeon[0])):
                for dx,dy in dirs:
                    if isWithin(dungeon, row + dx, col + dy):
                        if dungeon[row][col] > 0:
                            worst[row][col] = max(worst[row][col], worst[row +dx][col + dy])
                        else:
                            worst[row][col] = max(worst[row][col], worst[row +dx][col + dy] + dungeon[row][col])

        # print(min(worst))
        absolute_worst = -min(min(worst)) + 1 

        l = 1
        r = absolute_worst
        min_health = absolute_worst
        while l <= r:
            recreated = [[float('-inf') for k in i] for i in dungeon]
            m = (l + r )//2
            recreated[0][0] = m + dungeon[0][0]
            if recreated[0][0] <=0:
                l = m + 1
                continue
            for row in range(len(recreated)):
                for col in range(len(recreated[0])):
                    if row ==0 and col == 0:
                        continue
                    
                    for dx,dy in dirs:
                        if isWithin(recreated, row +dx, col + dy):

                            recreated[row][col] = max(recreated[row][col], dungeon[row][col] + recreated[row + dx][col + dy])              
                    if recreated[row][col] <= 0:
                        recreated[row][col] = float('-inf')
            
            final = recreated[-1][-1]
            print(m,recreated,final)

            if final <= 0:
                l = m +1
            else:
                min_health = min(m, min_health)
                r = m - 1
        return min_health




