class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        letters = [0] * 26

        for i in tiles:
            index = ord(i) - ord("A")
            letters[index] += 1
        ans = [0]

        def dfs(k):
            if k >= len(tiles):
                ans[0] += 1
                return
            
            for i in range(len(letters)):
                if letters[i] > 0:
                    letters[i] -= 1
                    dfs(k + 1)
                    letters[i] += 1


        for i in range(len(tiles)):
            dfs(i)
        return ans[0]



                
