class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        
        ans = []
        seen = set()
        def compute(expression, used):
            key = tuple(sorted(used))
            if key in seen:
                return
            seen.add(key)
            # print(expression)
            if len(expression) == 1:
                ans.append(expression[0][0])
                return expression[0][0]
            

            for i in range(2, len(expression), 2):
                operator = expression[i - 1][0]
                a = expression[i - 2][0]
                b = expression[i][0]
                if operator == "+":
                    c = a + b
                elif operator == "-":
                    # print(a,b)
                    c = a - b
                else:
                    c = a*b
                right = expression[i][2]
                left = expression[i- 2][1]
                
                compute(expression[0:i - 2] + [(c,left,right)] + expression[i + 1:], used + [(left,right)])

        init = []
        # compute(init,[] )
        running = []
        for i in expression:
            if i in ("+","-","*"):
                init.append(int("".join(running)))
                init.append(i)
                running = []
            else:
                running.append(i)
        init.append(int("".join(running)))
        # print(init)
        init = [ (i, index, index) for index,i in enumerate(init)]
        compute(init, [])


        return ans



            