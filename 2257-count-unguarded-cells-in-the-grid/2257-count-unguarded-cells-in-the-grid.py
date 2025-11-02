class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        guards= [ (i[0],i[1]) for i in guards]
        walls = [(i[0],i[1]) for i in walls]
        guards = set(guards)
        walls = set(walls)

        guarded = [[False for _ in range(n)] for _ in range(m)]
        def checkRow(direction):
            nonlocal m,n,guards,walls, guarded
            for i in range(m):
                guarding = False
                if direction > 0:
                    for j in range(n):
                        if (i,j) in guards:
                            guarding = True
                        if (i,j) in walls:
                            guarding = False
                        guarded[i][j] = guarded[i][j] | guarding
                else:
                    for j in range(n-1,-1,-1):
                        if (i,j) in guards:
                            guarding = True
                        if (i,j) in walls:
                            guarding = False
                        guarded[i][j] = guarded[i][j] | guarding

        def checkCol(direction):
            nonlocal m,n,guards,walls, guarded
            for i in range(n):
                guarding = False
                if direction > 0:
                    for j in range(m):
                        if (j,i) in guards:
                            guarding = True
                        if (j,i) in walls:
                            guarding = False
                        guarded[j][i] = guarded[j][i] | guarding
                else:
                    for j in range(m-1,-1,-1):
                        if (j,i) in guards:
                            guarding = True
                        if (j,i) in walls:
                            guarding = False
                        guarded[j][i] = guarded[j][i] | guarding
        checkRow(1)
        checkRow(-1)
        checkCol(-1)
        checkCol(1)
        ans =0
        for row in range(m):
            for col in range(n):
                if guarded[row][col] or (row,col) in walls or (row,col) in guards:
                    ans+=1
        return m*n - ans

        print(guarded)

"""



"""