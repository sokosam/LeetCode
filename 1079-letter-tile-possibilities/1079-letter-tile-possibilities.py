class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        letters = [0] * 26

        for i in tiles:
            index = ord(i) - ord("A")
            letters[index] += 1

        ans = set()

        def dfs(k, curr):
            if k >= len(tiles):
                ans.add(curr)
                return

            for i in range(len(letters)):
                if letters[i] > 0:
                    letters[i] -= 1
                    dfs(k + 1, curr + chr(i + ord('A')))
                    letters[i] += 1
            dfs(k + 1, curr)
                
        dfs(0, "")
        return len(ans) - 1



                
