class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        cols = [[]for _ in range(len(boxGrid))]

        for row in range(len(boxGrid)):
            items = 0
            for col in range(len(boxGrid[row])):
                if boxGrid[row][col] == "#":
                    items += 1
                elif boxGrid[row][col] == "*":
                    cols[row].append([items, len(boxGrid[0]) - col - 1])
                    items = 0
            cols[row].append([items,-1])
        cols.reverse()
        print(cols)

        ans = [["." for _ in range(len(boxGrid))] for _ in range(len(boxGrid[0]))]

        for col in range(len(cols)):
            while cols[col]:
                curr = cols[col].pop()
                index = curr[1]
                amt = curr[0]
                if index == -1:
                    for i in range(0,amt):
                        ans[i][col] = "#"
                else:
                    ans[index][col] = "*"
                    for i in range(index + 1, index + 1 + amt):
                        ans[i][col] = "#"
        return ans[::-1]

