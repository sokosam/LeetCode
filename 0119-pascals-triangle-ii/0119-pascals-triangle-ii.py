class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        count = 0
        left = 0
        ans = [1]
        while count < rowIndex:
            count += 1
            left = 0
            for i in range(len(ans)):
                temp = ans[i]
                ans[i] = left + ans[i]
                left = temp
            ans.append(1)
        return ans
