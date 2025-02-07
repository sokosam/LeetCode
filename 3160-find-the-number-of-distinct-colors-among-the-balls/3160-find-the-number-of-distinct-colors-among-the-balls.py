class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = {}
        vals = [0]* (limit + 1)
        ans = []
        curr = 0
        for i in queries:
            index = i[0]
            color = i[1]
            if vals[index] != 0 and colors[vals[index]] == 1:
                curr -=1
                colors[vals[index]] -= 1
            elif vals[index] != 0:
                colors[vals[index]] -=1
            vals[index] = color
            if color in colors:
                colors[color] +=1
            else:
                colors[color] = 1
            if colors[color] ==1:
                curr +=1
            ans.append(curr)
        return ans
