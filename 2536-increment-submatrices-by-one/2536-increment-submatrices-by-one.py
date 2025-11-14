class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        """

        first process all queries

        for any query:
            we are given x0,y0 and x1,y1

            given a query (0,0,1,1)
            [1,1,0]         [0,0] [1,1] [0,1] [0,1] [2,0][2,1]
            [0,0,0]
            [-1,-1,0]

            [1,1,0]
            [1,1,0]
            [0,0,0]

        


        """
        grid = [[0] * n for _ in range(n)]

        prefix = [[0]*n for _ in range(n)]

        for query in queries:
            x0,y0,x1,y1 = query
            prefix[x0][y0] +=1
            if y1 + 1 < n:
                prefix[x0][y1 + 1] -=1
            
            if x1 + 1 < n:

                prefix[x1 + 1][y0] -=1
                if y1 + 1< n:
                    prefix[x1 + 1][y1 + 1] +=1

        """
[[1, 0, -1], would turn into : [1, 1, 0]
 [0, 1, 0],                    [0, 1, 1]
[-1, 0, 1]]                    [-1, -1, 0]

        ultimate array = 
        [1, 1, 0]
        [1, 2, 1]
        [0, 1, 1]
        """

        newPrefix = [[0]*n for _ in range(n)]
        for row in range(n):
            running_sum = 0
            for col in range(n):
                running_sum += prefix[row][col]
                newPrefix[row][col] = running_sum

        for col in range(n):
            running_sum = 0
            for row in range(n):
                running_sum += newPrefix[row][col]
                grid[row][col] = running_sum
        return grid