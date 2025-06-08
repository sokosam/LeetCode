class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """

        n = 100
        1, 10, 100 , 1000 ... etc
        11, 110, 1100... etc
        12, 120, 1200,

        [1,2,3,4,5,6,7,8,9]

        n = 102

        1, 10, 100, 101, 102, 11, 12, 13, 14.. 19,


        """

        ans = []
        bases = [0,1,2,3,4,5,6,7,8,9]

        def dfs(curr, ans):
            if curr > n:
                return
            
            ans.append(curr)
            for i in bases:
                x = curr * 10
                dfs(x + i, ans)
        for i in bases:
            if i == 0:
                continue
            dfs(i, ans)
        return ans
    



