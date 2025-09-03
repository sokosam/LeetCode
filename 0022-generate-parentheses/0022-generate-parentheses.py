class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """

            ()
            () () , (())
            () () (), ((())), (()) (), () (())


            [(()(]
                (
            ((      ()
        (((  (())  ()(  ()
          ((()))


        """
        ans = []
        def helper(curr, leftBrackets, rightBrackets):
            nonlocal ans, n
            if len(curr) == 0:
                leftBrackets += 1
                helper(curr + "(", leftBrackets, rightBrackets)
            elif len(curr) == 2*n and leftBrackets == rightBrackets:
                ans.append(curr)
                return
            elif len(curr) > 2*n:
                return
            elif leftBrackets == rightBrackets:
                leftBrackets += 1
                helper(curr + "(", leftBrackets, rightBrackets )
            else:
                helper(curr + "(", leftBrackets + 1, rightBrackets )
                helper(curr + ")", leftBrackets, rightBrackets + 1)
        helper("",0,0)
        return ans

            

