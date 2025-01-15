class Solution:
    def calculate(self, s: str) -> int:
        

        def evaluate(start, value):
            if len(value) == 0:
                return 0, 0

            ans = 0
            sign = 1
            i = start
            while i < len(s) and value[i] != ')':
                if value[i] == '(':
                    val , pos = evaluate(i + 1,value)
                    ans += sign*  val
                    i = pos
                elif value[i] == '-':
                    sign = -1
                elif value[i] == '+':
                    sign = 1
                elif value[i].isnumeric():
                    ans += sign *int(value[i])
                i+=1

            return ans, i
        
        index =0 
        ans = 0
        while index < len(s):
            sm , index = evaluate(index, s)
            ans += sm
        # ans, pos = evaluate(0, s)
        # print(ans, pos)
        return ans
