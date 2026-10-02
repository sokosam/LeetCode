class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        """
        n = 1 : [()]
        n = 2 : [
                (()) ,
                 ()() 
                 ]
        n = 3 : [
            ((())),
            (()()),
            (())(),
            ()(()),
            ()()()
        ]
    
        """
        ans = set()
        para = []
        def bt(left, current):
            # print(current)
            nonlocal n
            if len(current) == 2*n:
                ans.add("".join(current))
                return

            right = len(current) - left
            if left == n:
                current.append(")")
                bt(left, current)
                current.pop()
                return

            if left == right:
                current.append("(")
                bt(left + 1, current)
                current.pop()
                return
            
            if left > right:
                current.append("(")
                bt(left + 1, current)
                current.pop()

                if right < n:
                    current.append(")")
                    bt(left , current)
                    current.pop()
                return
                    

        bt(0,[])
        return list(ans)

