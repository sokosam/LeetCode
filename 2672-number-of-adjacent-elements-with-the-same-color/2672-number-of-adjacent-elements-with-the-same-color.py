class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0]*(n + 2)
        ans = []
        adj = 0
        for query in queries:


            index = query[0] + 1
            color = query[1]

            if color == colors[index]:
                ans.append(adj)
                continue
            elif colors[index - 1] == colors[index] == colors[index + 1] and colors[index] != 0:
                adj -= 2
            elif colors[index - 1] == colors[index] and colors[index] != 0:
                adj -= 1
            elif colors[index + 1] == colors[index] and colors[index] != 0:
                adj -= 1
            

            colors[index] = color
            if colors[index - 1] == colors[index] == colors[index + 1]:
                adj +=2
            elif colors[index - 1] == colors[index] and colors[index] != 0:
                adj += 1
            elif colors[index + 1] == colors[index] and colors[index] != 0:
                adj += 1    
            ans.append(adj)
        return ans
